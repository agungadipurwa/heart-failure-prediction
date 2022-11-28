import pandas as pd
import streamlit as st
import requests

df = pd.read_csv("heart.csv")
# Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease
# 40, M, ATA, 140, 289, 0, Normal, 172, N, 0, Up, 0
def run():
    st.title("Heart Failure Prediction")
    age = st.number_input("Age")
    sex = st.selectbox("Sex", df.Sex.unique())
    chest_pain_type = st.selectbox("Chest Pain Type", df.ChestPainType.unique())
    resting_bp = st.number_input("Resting BP")
    cholesterol = st.number_input("Cholesterol")
    fasting_bs = st.selectbox("Fasting BS", df.FastingBS.unique())
    resting_ecg = st.selectbox("Resting ECG",df.RestingECG.unique())
    max_hr = st.number_input("Max HR")
    exercise_angina = st.selectbox("Exercise Angina", df.ExerciseAngina.unique())
    oldpeak = st.number_input("Old Peak")
    st_slope = st.selectbox("ST Slope", df.ST_Slope.unique())

    data ={
        'Age': int(age),
        'Sex': str(sex),
        'ChestPainType': str(chest_pain_type), 
        'RestingBP': int(resting_bp),
        'Cholesterol': int(cholesterol),
        'FastingBS': int(fasting_bs),
        'RestingECG': str(resting_ecg),
        'MaxHR': int(max_hr),
        'ExerciseAngina': str(exercise_angina),
        'Oldpeak': float(oldpeak),
        'ST_Slope': str(st_slope)
    }

    if st.button("Predict"):
        response = requests.post("http://ec2-108-137-4-27.ap-southeast-3.compute.amazonaws.com:8085/predict", json=data)
        prediction = response.text
        if prediction == "0":
            st.caption(f"The prediction from model: {prediction}")
            st.success("The model predict you are safe")
        else:
            st.success("The model predict you have heart disease")
            st.caption(f"The prediction from model: {prediction}")
if __name__ == '__main__':
    run()
