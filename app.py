from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
import requests
from datetime import datetime, timedelta

app = Flask(__name__)


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


# p8 api key : 3becb1759da057bd3b63a18a7d85d605
# additional api key : a611e8a7d5445b9bd6be0b38b647e4f1
api_key = '2172df3f3aff0c6287a4c7e14b54fb9e'  
  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_current_weather')
def fetch_current_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Kalaburagi&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
   
    return jsonify({
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed']
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['temp_lag1'], data['humidity_lag1'], data['pressure_lag1'], data['wind_speed_lag1']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
