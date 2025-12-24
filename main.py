from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

# 1. Load the model
import joblib
model = joblib.load('model.pkl')

# 2. Define the data structure (matches your Streamlit inputs)
class PricePredict(BaseModel):
    year: int
    km_driven: int
    fuel: int
    seller_type: int
    transmission: int
    owner: int
    engine: float
    max_power: float
    seats: float

@app.get('/')
def greet():
    return {"message": "Car Price API is running. Go to /docs to test."}

@app.post('/predict')
def predict(data: PricePredict):
    # 1. Convert input to dict
    data_dict = data.model_dump()
    
    # 2. REMOVE 'seats' (This reduces features from 9 to 8)
 
    
    # 3. Convert to array
    input_df = pd.DataFrame([data_dict])
    input_data_as_array = input_df.values
    
    # 4. Make prediction
    prediction = model.predict(input_data_as_array)[0]
    

    return {"price": float(prediction)}
