import os

from flask import Flask, render_template, request, url_for, redirect
import pickle

model_name = 'mlflowModel.pkl'
#model_name = os.environ['MODEL_NAME']
model = pickle.load(open(model_name, 'rb'))
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    params = None
    result = ""
    if request.method == 'POST':
        params = request.form
        result = model.predict(params)
    return render_template('index.html', params=params, result=result)

