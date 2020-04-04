# Code for the main server NodeMCU sends requests to

from flask import Flask, request, jsonify
from publisher import AgriIOTPublisher
import json


pub = AgriIOTPublisher()
topic = pub.getExistingTopicPath("main")


server = Flask(__name__)

@server.route("/", methods=["GET"])
def index():
    return "<h3>AgriIOT Cloud Backend</h3>", 200


@server.route("/api/data", methods=["POST"])
def data():
    try:
        timestamp = request.json["timestamp"]
        soil_moisture = request.json["soil_moisture"]
        temperature_humidity = request.json["temperature_humidity"]
        acoustic = request.json["acoustic"]

        nodemcu_data = json.dumps({
            "timestamp": timestamp,
            "soil_moisture": soil_moisture,
            "temperature_humidity": temperature_humidity,
            "acoustic": acoustic
        })

        pub.sendMessage(topic, nodemcu_data)
    
        success_resp = {
            "status": "ok",
            "error": "none"
        }

        return jsonify(success_resp), 200
    
    except Exception as e:
        error_resp = {
            "status": "fail",
            "error": str(e)
        }

        return jsonify(error_resp), 400


if __name__ == "__main__":
    server.run(port=3000, debug=True)