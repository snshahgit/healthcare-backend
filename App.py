import streamlit as st
import joblib
import requests
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_player import st_player

import streamlit.components.v1 as components
transformer = joblib.load('transformer.sav')
pca = joblib.load('pca.sav')
ada = joblib.load('ada.sav')
st.set_page_config(layout="wide")
with st.sidebar:
    
    choose = option_menu("Welcome", ["Home", "Tech Stack","Predictor","ML Code", "Contributors"],
                         icons=['house', 'stack', 'cpu','terminal', 'people-fill'],
                         menu_icon="activity", default_index=0, 
                         styles={
                            "container": {"padding": "5!important", "background-color": "#1a1a1a"},
                            "icon": {"color": "White", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4d4d4d"},
                            "nav-link-selected": {"background-color": "#4d4d4d"},
                        }
    ) 

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

with open("contributors.html",'r') as f:
   contributors=f.read();
def html():
    components.html(
      contributors
     ,
    height=1400,
    
    scrolling=True,
)
def pred():
    st.title("TYPE-2 DIABETES PREDICTOR")
    st.subheader("For women above 21 years of age")
    
    Glucose =st.number_input("",max_value=250)
    st.write("Glucose (mmol / L)")
    
    BloodPressure=st.number_input("",max_value=200)
    st.write("BloodPressure (mm Hg)")
    
    SkinThickness=st.number_input("",max_value=100)
    st.write("SkinThickness (Triceps skin fold thickness in mm)")
    
    Insulin=st.number_input("",max_value=251)
    st.write("Insulin (mu U/ml)")
    
    height=st.number_input("",min_value= 60, max_value=220)
    st.write("Height (in cm)")
    height/=100

    weight=st.number_input("",min_value= 30, max_value=170)
    st.write("Weight (in kg)")

    BMI= weight/(height**2)
    
    Pregnancies = st.slider("",0,10)
    st.write("Pregnancies (number)")
    

    Age=st.slider("",21, 85)
    st.write("Age (in years)")
    st.write("")
    DiabetesPedigreeFunction = np.random.uniform(-1.5,1.5, 1)[0]
    df = getData(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction,  Age=Age)
    

    df=helper(df)
    
    df = transformer.transform(df)
    
    piped_data = pca.transform(df)
    if(st.button("Submit")):
        ans = bool(int(ada.predict(piped_data)[0]))
        if ans:
            st.error("**The patient has high risk of Type-2 Diabetes**")
        else:
            st.success("**The patient has low risk of Type-2 Diabetes**")

with open('techstack.html','r') as f:
  techstack=f.read();
def tech():
    components.html(
    techstack
    ,
    height=1000,
    
    scrolling=True,
    )
def ml():
  st.write("To view the complete code for the end-to-end project, visit our [GitHub](https://github.com/snshahgit/healthcare-backend)")
  components.iframe("https://www.kaggle.com/embed/sns5154/type-2-diabetes-diagnosis-val-85-7-test-72-7?kernelSessionId=98362179",height=1000,)





if choose=="Predictor":

    pred()
elif choose=="Home":
    st.title('AI for Healthcare')
    st.markdown("<p style='text-align: justify;'>The objective of the project is to diagnostically predict whether or not a patient has Type 2 diabetes. \nThis predictor is built for Women above 21 years of age. The dataset, originally from the National Institute of Diabetes and Digestive and Kidney Diseases, used for this project consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.</p>", unsafe_allow_html=True)

    # st.markdown("<h1 style='text-align: center;'>Healthcare AI</h1>", unsafe_allow_html=True)

    with open("pic.html",'r') as f:
        pic=f.read();
    components.html(pic, height=400)

    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()
 
    # lt_url_hello = "https://assets6.lottiefiles.com/packages/lf20_1yy002na.json"
    # lottie_hello = load_lottieurl(lt_url_hello)
 
    # st_lottie(
    #         lottie_hello,  
    #         key="hello",
    #         speed=1,
    #         reverse=False,
    #         loop=True,
    #         quality="low",
    #         height=400,
    #         width=400            
    # )

    
elif choose=="Tech Stack":
    tech()
elif choose=="Contributors":
    html()
elif choose=="ML Code":
  ml()
