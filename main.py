from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Create FastAPI app
app = FastAPI(title="Car Price Prediction API")

# Load trained model
model = joblib.load("model.pkl")

# Input schema
class PricePredict(BaseModel):
from typing import Optional

class PricePredict(BaseModel):
    year: int
    km_driven: int
    fuel: int
    seller_type: int
    transmission: int
    owner: int
    engine: float
    max_power: float
    seats: Optional[float] = None

# Health check / root
@app.get("/")
def root():
    return {"status": "OK", "message": "Car Price API running. Visit /docs"}

# Prediction endpoint
@app.post("/predict")
def predict_price(data: PricePredict):

    # Convert input to dict
    input_data = data.model_dump()

    # REMOVE seats (model trained on 8 features)
    input_data.pop("seats")

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict
    prediction = model.predict(input_df)[0]

    return {
        "predicted_price": float(prediction)
    }

