# Serve model as a flask application
import pickle
import numpy as np
from flask import Flask, request

model = None
app = Flask(__name__)

# loading the saved trained model
def load_model():
    global model
    # model variable refers to the global variable
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

# for the index page: change according to what you want
@app.route('/')
def home_endpoint():
    return 'Usage:<br/> http://127.0.0.1:5000/predict?newCases=1000<br/>Hostname/IP address (Port): 127.0.0.1 (5000)<br/>GET parameter newCases'

@app.route('/predict', methods=['GET'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'GET':
        #data = request.get_json()  # Get data posted as a json
        # assuming the input will be sent as a GET parameter, e.g.,
        # http://127.0.0.1:5000/predict?newCases=10000
        data = request.args.get('newCases', type=int, default=0);
        data = np.array(data).reshape(1, -1)  # converts to numpy array and reshape 
        prediction = model.predict(data)  # runs globally loaded model on the data
    return str(int(prediction[0]))


#to find out the versio of python packages use the following commands
#inside python run-time environment
#from importlib.metadata import version
#version('construct')

if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=5000)
