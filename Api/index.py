from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    intensity: float
    velocity: float
    lat: float
    long: float
    tweet_count: int
    weather: int
    day: float
    hour: int


model = pickle.load(open('fmodel.pkl', 'rb'))
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

import numpy as np


@app.post('/model_prediction')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    intensity = input_dictionary['intensity']
    velocity = input_dictionary['velocity']
    lat = input_dictionary['lat']
    long = input_dictionary['long']
    tweet_count = input_dictionary['tweet_count']
    weather = input_dictionary['weather']
    day = input_dictionary['day']
    hour = input_dictionary['hour']
    data_point = np.array(
        [[intensity, velocity, lat, long, tweet_count, weather, day, hour]])  # Replace ... with your data
    scaled_data_point = scaler.transform(data_point)
    reshaped_data_point = np.reshape(scaled_data_point, (1, scaled_data_point.shape[1], 1))

    prediction = model.predict(reshaped_data_point)

    return prediction[0][0]
