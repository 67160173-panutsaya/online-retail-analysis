import streamlit as st
import joblib
import pandas as pd

model = joblib.load("sales_model.pkl")

st.title("Online Retail Sales Prediction")

quantity = st.number_input("Quantity")
unit_price = st.number_input("Unit Price")
country = st.number_input("Country Code")

if st.button("Predict"):

    input_data = pd.DataFrame({
    "Quantity":[quantity],
    "UnitPrice":[unit_price],
    "Country":[country]
})

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]}")