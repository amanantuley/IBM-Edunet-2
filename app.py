import streamlit as st
import pandas as pd
import joblib

model = joblib.load("bike_model.pkl")

st.title("🚲 Rental Bike Demand Predictor")

# Input Fields
temp = st.slider("Temperature (normalized)", 0.0, 1.0, 0.5)
hum = st.slider("Humidity", 0.0, 1.0, 0.5)
windspeed = st.slider("Windspeed", 0.0, 1.0, 0.2)
season = st.selectbox("Season", [1, 2, 3, 4])
yr = st.selectbox("Year (0=2011, 1=2012)", [0, 1])
mnth = st.slider("Month", 1, 12, 6)
holiday = st.selectbox("Holiday", [0, 1])
weekday = st.slider("Weekday", 0, 6, 3)
workingday = st.selectbox("Working Day", [0, 1])
weathersit = st.selectbox("Weather Situation", [1, 2, 3])
hr = st.slider("Hour", 0, 23, 12)
dayofweek = st.slider("Day of Week", 0, 6, 2)

input_df = pd.DataFrame([[temp, hum, windspeed, season, yr, mnth, holiday,
                          weekday, workingday, weathersit, hr, dayofweek]],
    columns=['temp', 'hum', 'windspeed', 'season', 'yr', 'mnth', 'holiday',
             'weekday', 'workingday', 'weathersit', 'hr', 'dayofweek'])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Bike Count: {int(prediction)}")
