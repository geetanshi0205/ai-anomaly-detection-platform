from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Patient Monitoring API Running"

@app.route("/vitals")
def vitals():

    data = {
        "heart_rate": random.randint(60,120),
        "spo2": random.randint(90,100),
        "temperature": 37
    }

    return jsonify(data)

app.run(debug=True)

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Patient Monitoring API Running"

@app.route("/vitals")
def vitals():

    data = pd.read_csv("patient_data.csv")

    latest = data.tail(1).to_dict(orient="records")

    return jsonify(latest)

app.run(debug=True)