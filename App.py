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
st.set_page_config(layout="wide")
with st.sidebar:
    
    choose = option_menu("Welcome", ["Home", "Tech Stack","Predictor","ML Code", "Creators"],
                         
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
def tech():
    
   
    components.html(
    """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap" rel="stylesheet">
    <title>Tech Stack</title>
    <style>
      *
{
    font-family: 'Ubuntu';
    /* zoom:94%; */
}

body {
  display: flex;
  width:100vw;
  height:100vh;
  justify-content: center;
  flex-wrap:wrap;
  align-items: center;
  font-family: Avenir, sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -moz-font-smoothing: antialiased;
  -webkit-font-smoothing: antialiased;
  font-smoothing: antialiased;
  background-color: black;

}

.tariffCards > div img
{
  margin: 10px 13px;
  height:50px;
  object-fit: cover;
  border-radius: 14px;
}
#Frontend>.premiumeconomy>img
{
  height:60px !important;
  margin-bottom: 5px !important;
}
#Frontend>.business>img
{
  height:60px !important;
  margin-bottom: 5px !important;
}
.tariffCards {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
  /* position: absolute; */
  user-select: none;
  transform: translate3d(0, 0, 0);
  transform-style: preserve-3d;
  margin:50px 50px;
  height:600px;
  
}
.tariffCards:after {
  position: absolute;
  bottom: -27px;
  left: 5%;
  content: '';
  width: 65%;
  height: 10px;
  border-radius: 100%;
  background-image: radial-gradient(rgba(34,50,84,0.04), rgba(34,50,84,0));
}
.tariffCards > div {
  /* position: relative; */
  width: 280px;
  height: 140px;
  border-radius: 12px;
  color: #fff;
  transform: rotateX(45deg) rotateY(-15deg) rotate(45deg);
  transition: all 0.4s ease;
  overflow: hidden;
  cursor: pointer;
  
}
.tariffCards > div:after {
  position: absolute;
  top: -70px;
  left: 0;
  content: '';
  width: 200%;
  height: 200%;
  background-image: linear-gradient(60deg, rgba(255,255,255,0) 20%, rgba(255,255,255,0.1), rgba(255,255,255,0) 80%);
  transform: translateX(-100%);
}

.tariffCards > div h2 {
  position: absolute;
  margin:10px 15px;
  font-size: 30px;
  font-weight: 1000;
}
.tariffCards > div span {
  position: absolute;
  font-weight: 700;
  bottom: 15px;
  left: 15px;
  font-size: 12px;
  font-weight: 600;
  opacity: 0.8;
}
.tariffCards > div.economy {
  margin-top: 0;
  z-index: 3;
  background-color: #8063e1;
  background-image: linear-gradient(135deg, #bd7be8, #8063e1);
  box-shadow: 20px 20px 60px rgba(34,50,84,0.5), 1px 1px 0px 1px #8063e1;
}
.tariffCards > div.premiumeconomy {
  margin-top: -70px;
  z-index: 2;
  background-color: #3f58e3;
  background-image: linear-gradient(135deg, #7f94fc, #3f58e3);
  box-shadow: 20px 20px 60px rgba(34,50,84,0.5), 1px 1px 0px 1px #3f58e3;
}
.tariffCards > div.business {
  margin-top: -70px;
  z-index: 1;
  background-color: #2c6fd1;
  background-image: linear-gradient(135deg, #21bbfe, #2c6fd1);
  box-shadow: 20px 20px 60px rgba(34,50,84,0.5), 1px 1px 0px 1px #2c6fd1;
}
.tariffCards > div.first {
  margin-top: -70px;
  background-color: #352f64;
  background-image: linear-gradient(135deg, #415197, #352f64);
  box-shadow: 5px 5px 60px rgba(34,50,84,0.1), 1px 1px 0px 1px #352f64;
}
.tariffCards > div:hover {
  transform: rotateX(30deg) rotateY(-15deg) rotate(30deg) translate(-25px, 50px);
}
.tariffCards > div:hover:after {
  transform: translateX(100%);
  transition: all 1.2s ease-in-out;
}
.tariffCards:active
{
  -webkit-tap-highlight-color: transparent;
}
a {
  position: fixed;
  bottom: 20px;
  right: 20px;
  color: #07f;
  font-size: 14px;
  font-weight: 700;
  width: 126px;
  height: 22px;
}

.card h1
{
    font-size:30px;
    margin-bottom:30px;
    background: linear-gradient(to right, #5bb3ff, #2c7ec5);
    padding: 10px 30px;
    border-radius: 10px;
    color:white;
    text-align: center;
    width:70%;
    height:18%;
    display: flex;
    align-items: center;
    justify-content: center;

}

html {
  scrollbar-width: normal;
  scrollbar-color: #777 #555;
}

html::-webkit-scrollbar {
  width: 2vw;
}

html::-webkit-scrollbar-thumb {
  background-color: #7418ff33;
}
img {
  pointer-events: none
}
.card 
{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height:600px;

}
    </style>
</head>
<body>
  <div class="card">
    <h1>Project <br> Management</h1>
    <div class="tariffCards" id="Frontend">
      <div class="economy">
        <img src="https://play-lh.googleusercontent.com/SWbS8z3NqFVHCEQc_6l-ZDdDj5qPGrWSK8hEWRSPHYm9s8958y6nTnoLolVHXlgKfXw" alt="">
        <h2>Asana</h2>
        
      </div>
      <div class="premiumeconomy">
        <img src="https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png" id="FrontEndCSS" alt="">
        <h2>Slack</h2>
      </div>
      <div class="business">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png"  alt="">
        <h2>Github</h2>
      </div>
    </div>
  </div>
  <div class="card">
    <h1>Machine <br> Learning</h1>
    <div class="tariffCards" id="Frontend">
      <div class="economy">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="">
        <h2>Sklearn</h2>
        
      </div>
      <div class="premiumeconomy">
        <img src="data:image/png;base64,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" id="FrontEndCSS" alt="">
        <h2>Numpy</h2>
      </div>
      <div class="business">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMIAAAEDCAMAAABQ/CumAAAAeFBMVEX///8TB1QAAEb/ygDnBIgPAFLNzNYTAFnQ0NgMAFcAAETb2eP39/oUBlfV1N7/xwDmAID/9tfLydcjG17/4Yz//vbCwM3ykcL61OfoBIwyKmgAADYAAE0AAErx8PTIxdT/+un/34T85/Lyir/lAHv50eX+9fkpH2Ma8J+4AAACEklEQVR4nO3dzVIaQRSAUYNCEIGoiYmJivnP+79hFrmLVHELZ6pnmG483xqaPruh5lb32ZkkSZIkSZIkvb52z7dZU2+rT4uH2X6rx6m31afF7M1+87dTb6tPCDWEUEMINYRQQ5MS1tu0nqtMSrhKn26e1v1WmZawyn58g4DQL4QIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECOFA6cvM5a4nYb29yjoO4WmVvM58WPQkbF8e+RqPcDlPVp4t+xLS/W0QEBCqI8yTLpsizN8n/WmJ0CEEBAQEBAQEBIT2CF+/fci6a4hw8y7rvC3CeRYCAgICAgICAgICAgICwlCEtJYIdzdp/3+kdkKHToFQ+RjJMCEcCKF7CAdC6B7CgRC6Nylh9zGtJUJ6uNCsnsOFhhkvPAHC9x+fsloi/Pp5nXTREuH++iLpMwICAgICAgICAgICAgKC/87R7/u0lggdQkBAQEBAQEB4dYQON67UTqh9KuwkDlRBQED4R8gOF5o3Rdh8yepLGO0ez6MNPO+WQ9w3NilhvBAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyEKJt+lL0SNeADUR4TG9cGWXHew10AkPP4aRBO9ohEuOFUEMINYRQQwg1dAKEDvd41t5t2u7lL0qSJEmSJEnSyfUXeomSFq0EzbkAAAAASUVORK5CYII="  alt="">
        <h2>Pandas</h2>
      </div>
      <div class="first">
        <img src="https://user-images.githubusercontent.com/315810/92161415-9e357100-edfe-11ea-917d-f9e33fd60741.png" alt="">
        <h2>Seaborn</h2>
      </div>
    </div>
  </div>
  <div class="card">
    <h1>Front-end</h1>
  <div class="tariffCards" id="Frontend">
    <div class="economy">
      <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" alt="">
      <h2>Javascript</h2>
      
    </div>
    <div class="premiumeconomy">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png" id="FrontEndCSS" alt="">
      <h2>CSS</h2>
    </div>
    <div class="business">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png"  alt="">
      <h2>HTML</h2>
    </div>
    <div class="first">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/1200px-Bootstrap_logo.svg.png" alt="">
      <h2>Bootstrap</h2>
    </div>
  </div>
  </div>


  <div class="card">
    <h1>Back-end</h1>
    <div class="tariffCards" id="Frontend">
      <div class="economy">
        <img src="https://avatars.githubusercontent.com/u/27804?s=280&v=4" alt="">
        <h2>Django</h2>
        
      </div>
      <div class="premiumeconomy">
        <img src="https://pbs.twimg.com/profile_images/1417542931209199621/fWMEIB5j_400x400.jpg" id="FrontEndCSS" alt="">
        <h2>FastAPI</h2>
      </div>
      <div class="business">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu6ff5XkzF2-XqAKaG3x9icDAh8dKp2-3gX4K4Hhruo5nQ5tJXoG9gr6uTQNznXkSf8q4&usqp=CAU"  alt="">
        <h2>Streamlit</h2>
      </div>
    </div>
  </div>
  
  <div class="card">
    <h1>Testing</h1>
    <div class="tariffCards" id="Frontend">
      <div class="economy">
        <img src="https://philnash.gallerycdn.vsassets.io/extensions/philnash/ngrok-for-vscode/1.9.2/1642679162508/Microsoft.VisualStudio.Services.Icons.Default" alt="">
        <h2>Ngrok</h2>
        
      </div>
      <div class="premiumeconomy">
        <img src="https://user-images.githubusercontent.com/2676579/34940598-17cc20f0-f9be-11e7-8c6d-f0190d502d64.png" id="FrontEndCSS" alt="">
        <h2>Postman</h2>
      </div>
      <div class="business">
        <img src="https://cdn.worldvectorlogo.com/logos/heroku-4.svg"  alt="">
        <h2>Heroku server </h2>
      </div>
    </div>
  </div>
  <div class="card">
    <h1>Deployment</h1>
    <div class="tariffCards" id="Frontend">
      <div class="economy">
        <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="">
        <h2>Docker</h2>
        
      </div>
      <div class="premiumeconomy">
        <img src="https://cdn.worldvectorlogo.com/logos/amazon-icon-1.svg" id="FrontEndCSS" alt="">
        <h2>AWS EC2</h2>
      </div>
      <div class="business">
        <img src="https://cdn.worldvectorlogo.com/logos/heroku-4.svg"  alt="">
        <h2>Heroku</h2>
      </div>
      
    </div>
  </div>
  
      
      
</body>
</html>
    """
    ,
    height=1000,
    
    scrolling=True,
    )
def ml():
  components.iframe("https://www.kaggle.com/embed/sns5154/type-2-diabetes-diagnosis-val-85-7-test-72-7?kernelSessionId=98362179",height=1000,)





if choose=="Predictor":

    pred()
elif choose=="Home":
    st.title('Type-2 Diabetes Predictor')
    st.write('The objective of the project is to diagnostically predict whether or not a patient has Type 2 diabetes. \nThis predictor is built for Women above 21 years of age. The dataset, originally from the National Institute of Diabetes and Digestive and Kidney Diseases, used for this project consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.')
elif choose=="Tech Stack":
    tech()
elif choose=="Creators":
    html()
elif choose=="ML Code":
  ml()
