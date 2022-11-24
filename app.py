import pandas as pd
import streamlit as st
import requests

df = pd.read_csv("model\heart.csv")
# Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease
# 40, M, ATA, 140, 289, 0, Normal, 172, N, 0, Up, 0
def run():
    st.title("Heart Failure Prediction")
    age = st.text_input("Age")
    sex = st.selectbox("Sex", df.Sex.unique())
    chest_pain_type = st.selectbox("Chest Pain Type", df.ChestPainType.unique())
    resting_bp = st.text_input("Resting BP")
    cholesterol = st.text_input("Cholesterol")
    fasting_bs = st.selectbox("Fasting BS", df.FastingBS.unique())
    resting_ecg = st.selectbox("Resting ECG",df.RestingECG.unique())
    max_hr = st.text_input("Max HR")
    exercise_angina = st.selectbox("Exercise Angina", df.ExerciseAngina.unique())
    oldpeak = st.number_input("Old Peak")
    st_slope = st.selectbox("ST Slope", df.ST_Slope.unique())

    data ={
        'Age': age,
        'Sex': sex,
        'ChestPainType': chest_pain_type, 
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG': resting_ecg,
        'MaxHR': max_hr,
        'ExerciseAngina': exercise_angina,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope
    }

    if st.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction = response.text
        st.success(f"The prediction from model: {prediction}")
if __name__ == '__main__':
    run()
