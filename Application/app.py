import streamlit as st
import numpy as np
import joblib
import os

# Use relative paths for deployment
scaler = joblib.load(os.path.join(os.path.dirname(__file__), "scaler.pkl"))
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))

st.title("Real Estate Price Predictor")

st.divider()

bed = st.number_input("Number of Bedrooms", value=2, step=1)
bath = st.number_input("Number of Bathrooms", value=1, step=1)
house_size = st.number_input("House Size (sq ft)", value=1000, step=50)

X = [bed, bath, house_size]

st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    st.write(f"Predicted House Price: ${prediction:,.2f}")
else:
    st.write("Please enter all the values to make a prediction.")

st.text("Made with ❤️ by Daivagna")
