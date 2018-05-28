from datetime import datetime

from bson import json_util
from flask import Flask, jsonify, request, json
from pymongo import MongoClient
from werkzeug.exceptions import BadRequest

from . import settings

app = Flask(__name__)

# Replace Flask dumps by Mongo BSON dumps
json.dumps = json_util.dumps


def get_mongo_client():
    return MongoClient(settings.MONGO_URI)


def get_log_db():
    client = get_mongo_client()
    return client.log


@app.route("/", methods=['GET'])
def ok():
    return "ok"


@app.route("/event", methods=['POST'])
def new_event():
    if not request.json or not request.json.get('name'):
        return BadRequest('Event must have a name')

    event = {
        'type': 'event',
        'name': request.json.get('name'),
        'segmentation': request.json.get('segmentation', {}),
        'timestamp': request.json.get('timestamp', datetime.utcnow()),
        'device_id': request.json.get('device_id'),
        'request_id': request.json.get('request_id'),
        'session_id': request.json.get('session_id'),
        'user_id': request.json.get('user_id'),
        'business_id': request.json.get('business_id'),
    }

    events = get_log_db().events
    inserted_id = events.insert_one(event).inserted_id
    inserted_event = events.find_one({'_id': inserted_id})
    return jsonify(inserted_event)


@app.route("/event", methods=["GET"])
def list_events():
    events = get_log_db().events
    return jsonify([event for event in
                    events.find().sort('timestamp', -1).limit(1000)])


@app.route("/request", methods=["POST"])
def new_request():
    mandatory_request_attrs = [
        "agent",
        "user_id",
        "bytes",
        "client_ip",
        "host",
        "referrer",
        "path",
        "request_time",
        "request_id",
        "timestamp",
        "verb",
        "request_body",
        "request_headers",
        "response_status",
        "response_headers",
        "response_body",
        "api_version",
    ]

    for attr in mandatory_request_attrs:
        if attr not in request.json:
            return BadRequest("'{}' is a required "
                              "Request attribute".format(attr))

    requests = get_log_db().requests
    inserted_id = requests.insert_one(request.json).inserted_id
    inserted_event = requests.find_one({'_id': inserted_id})
    return jsonify(inserted_event)


@app.route("/request", methods=["GET"])
def list_requests():
    requests = get_log_db().requests
    return jsonify([req for req in
                    requests.find().sort('timestamp', -1).limit(1000)])
