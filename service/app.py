from flask import Flask, request, jsonify
import yaml
import json
import logging.config

from settings import dictConfig
from utils.health_check import bringIntoLB, bringOutOfLB, poll
from service.handler.reco_handler import RecoHandler

app = Flask(__name__)
config = yaml.load(open('config.yml'))

logging.config.dictConfig(dictConfig)
error_logger = logging.getLogger('error_logger')
flask_logger = logging.getLogger('flask_logger')
resources_dir = config["resource_dir"]

reco_handler = RecoHandler(resources_dir)


@app.route('/api/v1/getRelevance', methods=['POST'])
def get_relevance():
    response = {
        "is_valid": "-1"
    }
    try:
        validity, status_code = reco_handler.get_relevance(request)
        response["is_valid"] = str(validity)
    except Exception as e:
        error_logger.error("Exception occurred", exc_info=True)
        return jsonify(response), 500
    error_logger.error(str(response))
    return jsonify(response), status_code



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



#app.run(host='0.0.0.0', port=6501, debug=config["debug"])
flask_logger.info("Ready to accept")
