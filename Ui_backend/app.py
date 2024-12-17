import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "UI Backend is running!"

@app.route("/predict")
def get_prediction():
    # Call the AI backend for predictions
    response = requests.get("http://ai_backend:5000/predict")
    return jsonify({"prediction": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
