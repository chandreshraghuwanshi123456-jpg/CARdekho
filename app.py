import streamlit as st 
import requests

# ⚠️ CHANGE THIS URL:
# For local testing use: 'http://127.0.0.1:8000/predict'
# For Render deployment use: 'https://cardekho-as2f.onrender.com/predict'
API = 'https://cardekho-as2f.onrender.com/predict'

st.title("🚗 Car Price Prediction")

# Input Fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
fuel = st.selectbox("Fuel Type (0:Diesel, 1:Petrol, 2:CNG, 3:LPG)", [0,1,2,3])
seller_type = st.selectbox("Seller Type (0:Indiv, 1:Dealer, 2:Trust)", [0,1,2])
transmission = st.selectbox("Transmission (0:Manual, 1:Auto)", [0,1])
owner = st.selectbox("Owner Type (0-4)", [0,1,2,3,4])
engine = st.number_input("Engine Size (CC)", min_value=500, step=50)
seats = st.number_input("Number of Seats", min_value=1.0, max_value=10.0, step=1.0)

# max_power is NOT needed by the model, so we don't send it.

if st.button('Predict Now'):
    # Prepare data dictionary - Keys must match main.py exactly
    input_data = {
        "year": int(year),
        "km_driven": int(km_driven),
        "fuel": int(fuel),
        "seller_type": int(seller_type),
        "transmission": int(transmission),
        "owner": int(owner),
        "engine": float(engine),
        "seats": float(seats)
    }

    try:
        response = requests.post(API, json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"💰 Predicted Price: ₹{result['predicted_price']:,.2f}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        st.error(f"Could not connect to Backend: {e}")

