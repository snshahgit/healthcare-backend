import pandas as pd

def helper(df):
    
    for idx, row in df.iterrows():
        if df.loc[idx, 'Pregnancies']> 13:
            df.loc[idx, 'Pregnancies'] = 13


    for idx, row in df.iterrows():
        if df.loc[idx, 'Glucose']> 200:
            df.loc[idx, 'Glucose'] = 200

        if df.loc[idx, 'Glucose']< 40:
            df.loc[idx, 'Glucose'] = 40


    for idx, row in df.iterrows():
        if df.loc[idx, 'BloodPressure']> 107:
            df.loc[idx, 'BloodPressure'] = 107

        if df.loc[idx, 'BloodPressure']< 35:
            df.loc[idx, 'BloodPressure'] = 35


    for idx, row in df.iterrows():
        if df.loc[idx, 'Insulin']> 323:
            df.loc[idx, 'Insulin'] = 323


    for idx, row in df.iterrows():
        if df.loc[idx, 'BMI']> 50:
            df.loc[idx, 'BMI'] = 50

        if df.loc[idx, 'BMI']< 14:
            df.loc[idx, 'BMI'] = 14
            
    
    for idx, row in df.iterrows():
        if df.loc[idx, 'DiabetesPedigreeFunction']> 1.19:
            df.loc[idx, 'DiabetesPedigreeFunction'] = 1.2
        

    for idx, row in df.iterrows():
        if df.loc[idx, 'Age']> 64:
            df.loc[idx, 'Age'] = 64
            
    
    return df


def getData(df=None, Pregnancies=None, Glucose= None, BloodPressure= None, SkinThickness= None, Insulin= None, BMI= None, DiabetesPedigreeFunction=None, Age= None):
    
    if df is None:
        df = pd.DataFrame({"Pregnancies":[Pregnancies], "Glucose":[Glucose], "BloodPressure":[BloodPressure], "SkinThickness":[SkinThickness], "Insulin":[Insulin], "BMI":[BMI], "DiabetesPedigreeFunction":[DiabetesPedigreeFunction], "Age": [Age]})
        return df
    
    elif type(df) == pd.DataFrame:
        # We have a DataFrame as an input
        df = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']]
        return df


