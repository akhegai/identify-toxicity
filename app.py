from flask import Flask, request, render_template, send_from_directory, make_response

from identify_toxicity.classificator.model import get_trained_model

app = Flask(__name__)

DEFAULT_TRAINED_MODEL_PATH = './models/'
classifier = get_trained_model(DEFAULT_TRAINED_MODEL_PATH)


@app.route('/api/classify', methods=['POST'])
def classify():
    print(request.data)
    classifier.predict()
    return ''
