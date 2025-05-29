import streamlit as st
import requests

st.title("NBA Over/Under Prediction")

# User input
rolling_pts_5 = st.number_input("Rolling PPG (last 5 games):", min_value=0.0, max_value=50.0, value=25.0)
is_home_game = st.selectbox("Is this a home game?", ["Yes", "No"]) == "Yes"

# Predict button
if st.button("Get Prediction"):
    payload = {
        "is_home_game": is_home_game,
        "rolling_pts_5": rolling_pts_5
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.markdown(f"### 🎯 Predicted Points: **{result['predicted_pts']}**")
        st.markdown(f"### 📈 Bet Suggestion: **{result['bet']}**")
        st.markdown(f"### 📊 Confidence: **{result['confidence'] * 100:.1f}%**")
    else:
        st.error("Something went wrong with the prediction.")
