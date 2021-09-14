import coloredlogs
import logging
import os
import random
import requests

from label_studio.ml import LabelStudioMLBase


class DigatorOpennlp(LabelStudioMLBase):
    def __init__(self, **kwargs):
        super(DigatorOpennlp, self).__init__(**kwargs)

        # Environment settings.
        os.environ.setdefault("DIGATOR_LOG_LEVEL", "INFO")
        self.digator_log_level = os.environ["DIGATOR_LOG_LEVEL"]

        os.environ.setdefault("DIGATOR_OPENNLP_URL", "http://127.0.0.1:8080/ner/news/ru/all?format=label-studio")
        self.digator_opennlp_url = os.environ["DIGATOR_OPENNLP_URL"]

        os.environ.setdefault("DIGATOR_SSL_VERIFY", "True")
        if os.environ["DIGATOR_SSL_VERIFY"].lower() == "true":
            self.digator_ssl_verify = True
        else:
            self.digator_ssl_verify = False

        # Logging.
        self.logger = logging.getLogger("digator_opennlp")
        coloredlogs.install(fmt="%(asctime)s %(name)s %(levelname)s %(message)s", level=self.digator_log_level)

    def predict(self, tasks, **kwargs):
        results = []

        for task in tasks:
            self.logger.debug("Received task: {}".format(task))

            try:
                r = requests.post(
                    self.digator_opennlp_url,
                    json={"text": task["data"]["text"]},
                    verify=self.digator_ssl_verify)

                results.append(r.json())
            except Exception as e:
                self.logger.error("Cannot connect to opennlp backend: {}".format(e))
                results.append({'result': [], 'score': 0})

        self.logger.debug("Send result to label studio: {}".format(results))
        return results

    def fit(self, completions, workdir=None, **kwargs):
        return {'random': random.randint(1, 10)}
