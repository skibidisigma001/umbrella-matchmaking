from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)
lobbies = []

@app.route("/match", methods=["GET"])
def match():
    global lobbies
    lobbies = [l for l in lobbies if time() - l["timestamp"] < 60]
    if lobbies:
        return jsonify({"status": "join", "ip": lobbies[0]["ip"], "port": lobbies[0]["port"]})
    else:
        return jsonify({"status": "host"})

@app.route("/host", methods=["POST"])
def host():
    data = request.json
    lobbies.append({
        "ip": data["ip"],
        "port": data["port"],
        "timestamp": time()
    })
    return jsonify({"status": "registered"})
