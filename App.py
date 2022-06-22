import streamlit as st
import joblib
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_player import st_player
import streamlit.components.v1 as components
transformer = joblib.load('transformer.sav')
pca = joblib.load('pca.sav')
ada = joblib.load('ada.sav')
with st.sidebar:
    
    choose = option_menu("Welcome", ["Home", "Tech Stack","Predictor", "Creators"],
                         
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

def html():
    components.html(
    """
    
   
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contributors</title>
    <link rel="stylesheet" href="cards.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/70d417915d.js" crossorigin="anonymous"></script>
    <style>
      *{
    font-family: 'Ubuntu';
    zoom: 95.1%;
}
a
{
    text-decoration: none;
}
body
{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    height:100%;
    width:100%;
}
.maincontainer
{
    margin:0px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    width:100%;
    height:100%;
    left:30%;
}
.maincard
{
    width:100%;
    display: flex;
    align-items: center;
    justify-content: center

}
.card
{
    /* max-width:15%; */
    width:270px;
    min-width:13%;
    height:410px;
    /* border:2px solid rebeccapurple; */
    border-radius: 10px;
    /* padding:10px; */
    margin:10px;
    display: flex;
    flex-direction:column ;
    justify-content: space-between;
    align-items: center;
    background-color: black;
    transition: all 0.3s ease-in-out;
}
.card2
{
    
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;

    /* min-width:100px; */
    width:100%;
}
.card1
{
    
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    width:100%;
    /* min-width:1000px; */
}
.name h1
{
    text-align: center;
    color:#ffffff;
}
.info
{
    height:60%;
    margin:15px 0px;
    color:white;
    width:80%;
    text-align: center;
}
.info h3
{
    margin:10px 0px;
    background-color: rgba(255, 255, 255, 0.15);
    padding:10px;
    border-radius: 10px;
    font-size:15px;
}

.name
{
    display:flex;
    justify-content:center;
    align-items: center;
    width:100%;
    height:200px;
    background-image: linear-gradient(to right,#c2587b,#c46f56);
    color: white;
    border-radius: 10px 10px 0px 0px;
}
.icons
{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 10px;

}
.icons i 
{
    display:block;
    padding:10px;
    font-size: 25px;
    color:#f2709c;
    cursor: pointer;
    transition: all ease-in-out 0.2s;

}
.eloper
{
    color:#c9c9c9;
    font-size:20px;
}
.links
{
    margin:12px 10px 10px 10px;
}
.icons i:hover
{
    /* font-size: 25px; */
    color:#c9c9c9;
}
.card:hover
{
    transform: translateY(-15px);
    box-shadow: rgba(0, 0, 0, 0.65) 0px 5px 15px;
    /* height:380px;
    width:270px; */

}
hr
{
    background-color: gray
}
html {
    scrollbar-width: normal;
    scrollbar-color: #777 #555;
  }

html::-webkit-scrollbar {
width: 1vw;
}

html::-webkit-scrollbar-thumb {
background-color: #7775;
}

html::-webkit-scrollbar-thumb:hover {
background-color: #777;
}

html::-webkit-scrollbar-track {
background-color: #5555;
}

html::-webkit-scrollbar-track:hover {
background-color: #555;
}

body {

color: #CCC;
}
    </style>

</head>
<body>
    <div class="maincontainer">
        <div class="card1">
           
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end </span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops </span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end </span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops </span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end </span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops r</span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end r</span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops </span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
        </div>
        <div class="card2">
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end </span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops </span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end </span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end </span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops </span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="card" >
                <div class="name"><h1>Shrey makadiya</h1></div>
                <div class="info">
                    <h3><span class="eloper">Front-end</span></h3>
                    <hr>
                    <h3><span class="eloper">Back-end</span></h3>
                    <hr>
                    <h3><span class="eloper">ML-ops</span></h3>

                    
                </div>
                <div class="links">
                    <div class="icons">
                       <a href="https://github.com/Neel1010" target="_blank"> <i class="fa-brands fa-github"></i></a>
                        <a href="https://www.kaggle.com/neelshah1010"><i class="fa-brands fa-kaggle"></i></a>	
                        <a href="linkedin.com/in/shah-neel-1010"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="tel:9512001311"><i class="fa-solid fa-phone"></i></a>
                        <a href="mailto: shahneel187@gmail.com">
                            <i class="fa fa-envelope"></i>
                        </a>
                    </div>
                    
                    
                </div>
                
            </div>
           

        </div>
        
        

       
        
    </div>
</body>
</html>
    """,
    height=1000,
    
    scrolling=True,
)
def pred():
    st.title("Diabetese Predictor for Women")
    
    Pregnancies = st.number_input("",max_value=10)
    st.write("Pregnancies")
    
    Glucose =st.number_input("",max_value=250)
    st.write("Glucose")
    
    BloodPressure=st.number_input("",max_value=200)
    st.write("BloodPressure")
    
    SkinThickness=st.number_input("",max_value=100)
    st.write("SkinThickness")
    
    Insulin=st.number_input("",max_value=251)
    st.write("Insulin")
    
    BMI=st.number_input("",max_value=33.0)
    st.write("BMI")
    
    Age=st.number_input("",max_value=99)
    st.write("Age")
    st.write("")
    DiabetesPedigreeFunction = np.random.uniform(-1.5,1.5, 1)[0]
    df = getData(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction,  Age=Age)
    

    df=helper(df)
    
    df = transformer.transform(df)
    
    piped_data = pca.transform(df)
    if(st.button("Submit")):
        ans = bool(int(ada.predict(piped_data)[0]))
        if ans:
            st.error("You Have Diabetese")
        else:
            st.success("You Do Not Have Diabetese")
if choose=="Predictor":

    pred()
elif choose=="Home":
    pass
elif choose=="Tech Stack":
    pass
elif choose=="Creators":
    html()
