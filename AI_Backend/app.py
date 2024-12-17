from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/predict")
def predict():
    # Example logic for prediction
    result = {"prediction": "This is a sample prediction"}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
