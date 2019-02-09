from flask import Flask, request, render_template, send_from_directory, make_response, jsonify

from identify_toxicity.classificator.model import Classifier
from identify_toxicity.constants.paths import TFIDF_BOW_PATH, TRAINED_NBSVM_PATH

app = Flask(__name__)

classifier = Classifier(TRAINED_NBSVM_PATH, TFIDF_BOW_PATH)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = classifier.predict(data)
    return jsonify(prediction)
