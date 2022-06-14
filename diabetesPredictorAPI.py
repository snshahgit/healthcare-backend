import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Pipeline import getData, helper
import joblib

transformer = joblib.load('transformer.sav')
pca = joblib.load('pca.sav')
ada = joblib.load('ada.sav')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/diabetesPredictorAPI")
def diabetesPredictorAPI(Pregnancies: int, Glucose: int, BloodPressure: int, SkinThickness: int, Insulin: int, BMI: float, Age: int):
    
    DiabetesPedigreeFunction = np.random.uniform(-1.5,1.5, 1)[0]
    # Since the Diabetes Pedigree Function is unknown to the end user,
    # We go by the inference from the training data i.e. the distribution
    # is uniform ranging from -1.5 to 1.5
        
    df = getData(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction,  Age=Age)
    df = helper(df)
    df = transformer.transform(df)
    piped_data = pca.transform(df)

    ans = bool(int(ada.predict(piped_data)[0]))
    if ans:
        ans= "Diabetic"
    else:
        ans= "Non-Diabetic"
    
    return(ans)

