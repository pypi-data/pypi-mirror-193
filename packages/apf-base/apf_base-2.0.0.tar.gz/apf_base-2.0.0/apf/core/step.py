from abc import abstractmethod
import abc
from typing import Any, List, Type, Union
from apf.consumers import GenericConsumer
from apf.metrics.generic import GenericMetricsProducer
from apf.producers import GenericProducer
from apf.core import get_class
from prometheus_client import Enum, Gauge, Summary, start_http_server
import logging
import datetime


class DefaultConsumer(GenericConsumer):
    def consume(self):
        yield {}


class DefaultProducer(GenericProducer):
    def produce(self, message, **kwargs):
        pass


class DefaultMetricsProducer(GenericMetricsProducer):
    def send_metrics(self, metrics):
        pass


class GenericStep(abc.ABC):
    """Generic Step for apf.

    Parameters
    ----------
    consumer : :class:`GenericConsumer`
        An object of type GenericConsumer.
    level : logging.level
        Logging level, has to be a logging.LEVEL constant.

        Adding `LOGGING_DEBUG` to `settings.py` set the step's global logging level to debug.

        .. code-block:: python

            #settings.py
            LOGGING_DEBUG = True

    **step_args : dict
        Additional parameters for the step.
    """

    def __init__(
        self,
        consumer: Type[GenericConsumer] = DefaultConsumer,
        producer: Type[GenericProducer] = DefaultProducer,
        metrics_sender: Type[GenericMetricsProducer] = DefaultMetricsProducer,
        config: dict = {},
        level: int = logging.INFO,
    ):
        self._set_logger(level)
        self.config = config
        self.consumer = self._get_consumer(consumer)(self.consumer_config)
        self.producer = self._get_producer(producer)(self.producer_config)
        self.init_prometheus_metrics()
        self.metrics_sender = self._get_metrics_sender(metrics_sender)(
            self.metrics_config
        )
        self.metrics = {}
        self.extra_metrics = []
        if self.metrics_config:
            self.extra_metrics = self.metrics_config.get("EXTRA_METRICS", ["candid"])
        self.commit = self.config.get("COMMIT", True)

    @property
    def consumer_config(self):
        return self.config["CONSUMER_CONFIG"]

    @property
    def producer_config(self):
        return self.config.get("PRODUCER_CONFIG", {})

    @property
    def metrics_config(self):
        return self.config.get("METRICS_CONFIG")

    def init_prometheus_metrics(self):
        if self.config.get("PROMETHEUS"):
            self.use_prometheus = True
            self.prometheus_consumed_messages = Summary(
                "consumed_messages", "Current number of messages consumed"
            )
            self.prometheus_processed_messages = Summary(
                "processed_messages", "Current number of messages processed"
            )
            self.prometheus_execution_time = Summary(
                "execution_time", "Execution time of processed batch"
            )
            self.prometheus_telescope_id = Enum(
                "telescope_id", "Id of the telescope", states=["ZTF", "ATLAS"]
            )

    def _set_logger(self, level):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(level)
        self.logger.info(f"Creating {self.__class__.__name__}")

    def _get_consumer(self, default: Type[GenericConsumer]) -> Type[GenericConsumer]:
        if self.consumer_config:
            Consumer = default
            if "CLASS" in self.consumer_config:
                Consumer = get_class(self.consumer_config["CLASS"])
            return Consumer
        raise Exception("Could not find CONSUMER_CONFIG in the step config")

    def _get_producer(self, default: Type[GenericProducer]) -> Type[GenericProducer]:
        Producer = default
        if "CLASS" in self.producer_config:
            Producer = get_class(self.producer_config["CLASS"])
        return Producer

    def _get_metrics_sender(
        self, default: Type[GenericMetricsProducer]
    ) -> Type[GenericMetricsProducer]:
        Metrics = default
        if self.metrics_config:
            if "CLASS" in self.metrics_config:
                Metrics = get_class(self.config["METRICS_CONFIG"].get("CLASS"))
        return Metrics

    def send_metrics(self, **metrics):
        """Send Metrics with a metrics producer.

        For this method to work the `METRICS_CONFIG` variable has to be set in the `STEP_CONFIG`
        variable.

        **Example:**

        Send the compute time for an object.

        .. code-block:: python

            #example_step/step.py
            self.send_metrics(compute_time=compute_time, oid=oid)

        For this to work we need to declare

        .. code-block:: python

            #settings.py
            STEP_CONFIG = {...
                "METRICS_CONFIG":{ #Can be a empty dictionary
                    "CLASS": "apf.metrics.KafkaMetricsProducer",
                    "PARAMS": { # params for the apf.metrics.KafkaMetricsProducer
                        "PARAMS":{
                            ## this producer uses confluent_kafka.Producer, so here we provide
                            ## arguments for that class, like bootstrap.servers
                            bootstrap.servers": "kafka1:9092",
                        },
                        "TOPIC": "metrics_topic" # the topic to store the metrics
                    },
                }
            }

        Parameters
        ----------
        **metrics : dict-like
            Parameters sent to the kafka topic as message.

        """
        if self.metrics_sender:
            metrics["source"] = self.__class__.__name__
            self.metrics_sender.send_metrics(metrics)

    def _pre_consume(self):
        if self.use_prometheus:
            self.logger.info("Starting metrics server")
            start_http_server(8000)
        self.logger.info("Starting step. Begin processing")
        self.pre_consume()

    def pre_consume(self):
        pass

    def _pre_execute(self, message: Union[dict, List[dict]]):
        self.logger.info("Received message. Begin preprocessing")
        self.metrics["timestamp_received"] = datetime.datetime.now(
            datetime.timezone.utc
        )
        if isinstance(message, dict):
            message = [message]
        self.message = message
        if self.use_prometheus:
            if isinstance(self.message, dict):
                self.prometheus_consumed_messages.observe(1)
                tid = self.message.get("tid")
                if tid:
                    tid = str(tid).upper()
                    self.prometheus_telescope_id.state(tid)
            if isinstance(self.message, list):
                self.prometheus_consumed_messages.observe(len(self.message))
                tid = self.message[0].get("tid")
                if tid:
                    tid = str(tid).upper()
                    self.prometheus_telescope_id.state(tid)
        preprocessed = self.pre_execute(self.message)
        return preprocessed or self.message

    def pre_execute(self, messages: List[dict]):
        pass

    @abstractmethod
    def execute(self, messages: List[dict]):
        """Execute the logic of the step. This method has to be implemented by
        the instanced class.

        Parameters
        ----------
        message : dict, list
            Dict-like message to be processed or list of dict-like messages
        """
        pass

    def _post_execute(self, result: Any):
        self.logger.info("Processed message. Begin post processing")
        final_result = self.post_execute(result)
        self.metrics["timestamp_sent"] = datetime.datetime.now(datetime.timezone.utc)
        time_difference = (
            self.metrics["timestamp_sent"] - self.metrics["timestamp_received"]
        )
        self.metrics["execution_time"] = time_difference.total_seconds()
        if self.extra_metrics:
            extra_metrics = self.get_extra_metrics(self.message)
            self.metrics.update(extra_metrics)
        self.send_metrics(**self.metrics)
        if self.use_prometheus:
            if isinstance(self.message, dict):
                self.prometheus_processed_messages.observe(1)
            if isinstance(self.message, list):
                self.prometheus_processed_messages.observe(len(self.message))
            self.prometheus_execution_time.observe(time_difference.total_seconds())
        return final_result

    def post_execute(self, result: Any):
        return result

    def _pre_produce(self, result: Any):
        self.logger.info("Finished all processing. Begin message production")
        message_to_produce = self.pre_produce(result)
        return message_to_produce

    def pre_produce(self, result: Any):
        return result

    def _post_produce(self):
        self.logger.info("Message produced. Begin post production")
        self.post_produce()

    def post_produce(self):
        pass

    def get_value(self, message, params):
        """Get values from a massage and process it to create a new metric.

        Parameters
        ----------
        message : dict
            Dict-like message to be processed

        params : str, dict
            String of the value key or dict with the following:

            - 'key': str
                Must have parameter, has to be in the message.
            - 'alias': str
                New key returned, this can be used to standarize some message keys.
            - 'format': callable
                Function to be call on the message value.

        Returns
        -------
        new_key, value
            Aliased key and processed value.

        """
        if isinstance(params, str):
            return params, message.get(params)
        elif isinstance(params, dict):
            if "key" not in params:
                raise KeyError("'key' in parameteres not found")

            val = message.get(params["key"])
            if "format" in params:
                if not callable(params["format"]):
                    raise ValueError("'format' parameter must be a calleable.")
                else:
                    val = params["format"](val)
            if "alias" in params:
                if isinstance(params["alias"], str):
                    return params["alias"], val
                else:
                    raise ValueError("'alias' parameter must be a string.")
            else:
                return params["key"], val

    def get_extra_metrics(self, message):
        """Generate extra metrics from the EXTRA_METRICS metrics configuration.

        Parameters
        ----------
        message : dict, list
            Dict-like message to be processed or list of dict-like messages

        Returns
        -------
        dict
            Dictionary with extra metrics from the messages.

        """
        # Is the message is a list then the metrics are
        # added to an array of values.
        if isinstance(message, list):
            extra_metrics = {}
            for msj in message:
                for metric in self.extra_metrics:
                    aliased_metric, value = self.get_value(msj, metric)
                    # Checking if the metric exists
                    if aliased_metric not in extra_metrics:
                        extra_metrics[aliased_metric] = []
                    extra_metrics[aliased_metric].append(value)
            extra_metrics["n_messages"] = len(message)

        # If not they are only added as a single value.
        else:
            extra_metrics = {}
            for metric in self.extra_metrics:
                aliased_metric, value = self.get_value(message, metric)
                extra_metrics[aliased_metric] = value
            extra_metrics["n_messages"] = 1
        return extra_metrics

    def start(self):
        """Start running the step."""
        self._pre_consume()
        for message in self.consumer.consume():
            preprocessed_msg = self._pre_execute(message)
            result = self.execute(preprocessed_msg)
            result = self._post_execute(result)
            result = self._pre_produce(result)
            self.producer.produce(result)
            self._post_produce()
        self._tear_down()

    def _tear_down(self):
        self.logger.info("Processing finished. No more messages. Begin tear down.")
        self.tear_down()
        self._write_success()

    def _write_success(self):
        f = open("__SUCCESS__", "w")
        f.close()

    def tear_down(self):
        pass
