import logging
import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():

    return render_template("index.html")


@app.route("/", methods=["POST"])
def post_image():

    file = request.files["file"]

    r = requests.post("....", files={"file": file})

    r.raise_for_status()
