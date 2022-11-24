from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s payload")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    # Performs an sklearn prediction
    try:
        # Load pretrained model as clf. Try any one model. 
        clf = joblib.load("./Housing_price_model/LinearRegression.joblib")
        # clf = joblib.load("./Housing_price_model/StochasticGradientDescent.joblib")
        # clf = joblib.load("./Housing_price_model/GradientBoostingRegressor.joblib")
        clf = clf[0][0]
    except:
        LOG.info("JSON payload: %s json_payload")
        return "Model not loaded"
    
    try:
        json_payload = request.json
    except e:
        return "request failed" + e
    
    LOG.info("JSON payload: %s json_payload")
    
    try:
        inference_payload = pd.DataFrame(json_payload)
        LOG.info("inference payload DataFrame: %s inference_payload")
    except:
        return "inference failed"
    
    try:
        scaled_payload = scale(inference_payload)
    except:
        return "scaling failed"
    
    try:
        prediction = list(clf.predict(scaled_payload))
    except:
        return "prediction failed"
    
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
