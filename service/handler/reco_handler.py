import yaml
import joblib
import json
import logging.config
import gc

from settings import dictConfig
from service.model.relevance_model import RelevanceModel


config = yaml.load(open('config.yml'))

logging.config.dictConfig(dictConfig)
error_logger = logging.getLogger('error_logger')
flask_logger = logging.getLogger('flask_logger')
resources_dir = config["resource_dir"]



class RecoHandler:
    def __init__(self):
        classifier_file = resources_dir + config["pickle"]["classifier_model_file"]
        processor_file = resources_dir + config["pickle"]["preprocess_model_file"]

        classifier = joblib.load(classifier_file)
        processor = joblib.load(processor_file)
        gc.collect()
        self.relevance_model = RelevanceModel(classifier=classifier, processor=processor)


    def is_valid_request(self, request):
        try:
            json_data = json.loads(request.data)
            text = json_data.get("text")
        except KeyError:
            error_logger.error("Bad request", exc_info=True)
            return False, None
        except Exception as e:
            error_logger.error("Exception occurred", exc_info=True)
            return False, None
            # print("Exception occured: " + str(traceback.print_exc()))
        return True, text

    def get_relevance(self, request):
        is_valid, text = self.is_valid_request(request)
        if not is_valid:
            return -1, 400
        validity = self.relevance_model.get_validity(text)
        return validity, 200