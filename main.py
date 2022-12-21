import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
from os.path import abspath


app = FastAPI(title='Heart Failure Prediction', version='1.0',
              description='Random Forest model is used for prediction')
# # model_path = abspath('HeartFailurePrediction.pkl')
model_path = abspath('./HeartFailurePrediction.pkl') #for my local dict
model = joblib.load(model_path)



class Data(BaseModel):
    Age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str


@app.get('/home')
def read_home():
    """
    Home endpoint which can be used to test the availability of the healt prediction application.
    """
    return {'message': 'System is healthy'}

@app.post("/predict")
def predict(data: Data):
    result = model.predict(pd.DataFrame(columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
                                                 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'],
                                        data=np.array([data.Age, data.Sex, data.ChestPainType, data.RestingBP, data.Cholesterol,
                                                       data.FastingBS, data.RestingECG, data.MaxHR, data.ExerciseAngina, data.Oldpeak,
                                                       data.ST_Slope]).reshape(1, 11)))

    
    return (result.tolist())[0]
    

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8090, reload=True)
