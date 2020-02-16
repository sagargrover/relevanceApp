from flask import Flask, request, jsonify
import yaml
import joblib
import traceback
import json
import logging.config
import gc

from settings import dictConfig
from service.model.relevance_model import RelevanceModel
from utils.health_check import bringIntoLB, bringOutOfLB, poll

app = Flask(__name__)
config = yaml.load(open('config.yml'))

logging.config.dictConfig(dictConfig)
error_logger = logging.getLogger('error_logger')
flask_logger = logging.getLogger('flask_logger')
resources_dir = config["resource_dir"]


classifier_file = resources_dir + config["pickle"]["classifier_model_file"]
processor_file = resources_dir + config["pickle"]["preprocess_model_file"]

classifier = joblib.load(classifier_file)
processor = joblib.load(processor_file)


relevance_model = RelevanceModel(classifier=classifier, processor=processor)

gc.collect()

@app.route('/api/v1/getRelevance', methods=['POST'])
def get_recommended_styles():
    # import ipdb; ipdb.set_trace()
    # error_logger.error('abc')
    # flask_logger.info("recommend for uidx: " + str() )
    # import ipdb; ipdb.set_trace()
    json_data = json.loads(request.data)
    text = json_data.get("text", "")
    try:
        validity = relevance_model.get_validity(text)
    except Exception as e:
        error_logger.error("Exception occurred", exc_info=True)
        return app.response_class(
            response=None,
            status=500,
            mimetype='application/json'
        )
        # print("Exception occured: " + str(traceback.print_exc()))
    return jsonify(validity)



@app.route('/health_check', methods=['GET'])
def get_heath_check():
    if poll(request):
        return json.dumps({"body": "IN"}), 200
    else:
        return json.dumps({"body": "OUT"}), 404


@app.route('/health/bringIntoLB', methods=['GET'])
def bring_into_lb():
    return bringIntoLB()


@app.route('/health/bringOutOfLB', methods=['GET'])
def bring_out_of_lb():
    return bringOutOfLB()



#app.run(host='0.0.0.0', port=6501, debug=config["debug"], use_reloader=False)
print("Ready to accept")
