import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Sales Prediction App",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<style>
.stButton>button {
    background-color: #03a9f4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Sales Prediction Dashboard")
st.markdown("ทำนายยอดขายจาก ราคา เวลา และประเทศ 🌍")

# โหลดโมเดล + encoder
model = joblib.load("sales_model.pkl")
le = joblib.load("encoder.pkl")
print(model.feature_names_in_)


# รับค่าจากผู้ใช้
unit_price = st.number_input("Unit Price", 0.0, 1000.0)
hour = st.slider("Hour", 0, 23)
month = st.slider("Month", 1, 12)

country_name = st.selectbox("Country", le.classes_)
country = le.transform([country_name])[0]



# 👇 แล้วค่อยเอาไปใช้
if st.button("Predict"):
    input_data = pd.DataFrame([[1, unit_price, hour, month]],
                          columns=['Quantity', 'UnitPrice', 'Hour', 'Month'])

    prediction = model.predict(input_data)

    st.success(f"Predicted Quantity: {prediction[0]}")