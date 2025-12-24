from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Car Price Prediction API")

# Load model
# Ensure scikit-learn version matches your local environment if possible
model = joblib.load("model.pkl")

# Input schema - MUST MATCH ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'engine', 'seats']
class PricePredict(BaseModel):
    year: int
    km_driven: int
    fuel: int
    seller_type: int
    transmission: int
    owner: int
    engine: float
    seats: float 

@app.get("/")
def root():
    return {"status": "OK", "message": "API is running. Visit /docs"}

@app.post("/predict")
def predict_price(data: PricePredict):
    # Convert Pydantic object to Dictionary
    data_dict = data.model_dump()
    
    # Create DataFrame (Columns will match because keys match)
    input_df = pd.DataFrame([data_dict])
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    return {"predicted_price": float(prediction)}
