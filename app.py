import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

TMB_APP_ID = os.getenv("TMB_APP_ID")
TMB_APP_KEY = os.getenv("TMB_APP_KEY")

STOPS = [
    {"id": 556, "name": "Zona Universitaria"},
    # TODO: find two stops from your own life and add them here
    # {"id": ???, "name": "Your stop name"},
    # {"id": ???, "name": "Your stop name"},
]

@app.route("/")
def index():
    stop_boards = []
    for stop in STOPS:
        url = f"https://api.tmb.cat/v1/ibus/stops/{stop['id']}"
        response = requests.get(url, params={"app_id": TMB_APP_ID, "app_key": TMB_APP_KEY})
        raw = response.json()["data"]["ibus"]
        arrivals = [
            {"line": bus["line"], "destination": bus["destination"], "text": bus["text-ca"]}
            for bus in raw
        ]
        stop_boards.append({
            "name": stop["name"],
            "arrivals": arrivals
        })
    return render_template("index.html", stop_boards=stop_boards)
