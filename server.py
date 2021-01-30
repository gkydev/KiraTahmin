from flask import Flask, render_template, request
import json
from predict import predict
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    if request.method == "POST":
        predict_data = {}
        for x in request.form:
            predict_data[x] = [int(request.form[x])]
        print(predict_data)
        data = predict(predict_data)
        return render_template('index.html',data=data)
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def apiPredict():
    if request.method == "POST":
        data = predict(request.json)
        return str(data)
    return "Error"
    
app.run(debug=True,use_reloader=False)