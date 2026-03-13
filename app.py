import streamlit as st
import pandas as pd
import joblib

st.title("Online Retail Sales Prediction")

model = joblib.load("sales_model.pkl")

st.header("Predict Product Quantity")

unit_price = st.number_input("Unit Price", 0.0, 1000.0)

hour = st.slider("Hour",0,23)

month = st.slider("Month",1,12)

country = st.number_input("Country Code",0,50)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "UnitPrice":[unit_price],
        "Hour":[hour],
        "Month":[month],
        "Country":[country]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Quantity: {prediction[0]}")