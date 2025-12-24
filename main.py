from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Car Price Prediction API")

# Load model
model = joblib.load("model.pkl")

# Input schema (MATCHES TRAINING FEATURES)
class PricePredict(BaseModel):
    year: int
    km_driven: int
    fuel: int
    seller_type: int
    transmission: int
    owner: int
    engine: float
    seats: float   # REQUIRED
    # ❌ max_power REMOVED

@app.get("/")
def root():
    return {"status": "OK", "message": "API is running. Visit /docs"}

@app.post("/predict")
def predict_price(data: PricePredict):

    # Convert to DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    # Predict
    prediction = model.predict(input_df)[0]

    return {"predicted_price": float(prediction)}
