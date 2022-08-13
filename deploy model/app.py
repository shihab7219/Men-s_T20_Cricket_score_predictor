import streamlit as st
import pickle
import pandas as pd
import base64
import numpy as np
import sklearn
from xgboost import XGBRegressor


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('image/Live-the-Game.png')




pipe = pickle.load(open("pipe2.pkl","rb"))

teams = ["Australia",
         "India",
         "Bangladesh",
         "New Zealand",
         "South Africa",
         "England",
         "West Indies",
         "Afghanistan",
         "Pakistan",
         "Sir Lanka"]

citis = ['Barbados', 'Mirpur', 'St Lucia', 'Johannesburg', 'Nagpur',
       'Birmingham', 'Ahmedabad', 'Wellington', 'Perth', 'Cardiff',
       'Pallekele', 'Paarl', 'Hambantota', 'London', 'Colombo', 'Lucknow',
       'Sydney', 'Bristol', 'Cape Town', 'Cuttack', 'Nairobi', 'Rajkot',
       'Visakhapatnam', 'Chittagong', 'Dubai', 'Dhaka', 'Auckland',
       'Kolkata', 'Harare', 'Lahore', 'Lauderhill', 'Hamilton',
       'Nottingham', 'Manchester', 'Trinidad', 'Taunton', 'Melbourne',
       'Napier', 'East London', 'Antigua', 'Mumbai', 'Indore', 'Durban',
       'Karachi', 'Gros Islet', 'Bengaluru', 'Southampton', 'Chattogram',
       'Chester-le-Street', 'St Kitts', 'Centurion', 'Guwahati',
       'St Vincent', 'Chennai', 'Adelaide', 'Basseterre', 'King City',
       'Pune', 'Chandigarh', 'Mount Maunganui', 'Delhi']


st.title("Man's T20 Crictket Score Predictor")

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batthing team",sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling team",sorted(teams))


city = st.selectbox("Select city",sorted(citis))

col3,col4,col5 = st.columns(3)

with col3 :
    current_socre = st.number_input("Current Socre")

with col4 :
    overs = st.number_input("Overs Done(works for over>5)")

with col5 :
    wickets = st.number_input("Wickets Out")


last_five = st.number_input("Runs soored in last 5 overs")

if st.button("Predict Score"):
    balls_left = 120-(overs*6)
    wickets_left = 10 -wickets
    crr = current_socre/overs

    input_df = pd.DataFrame(
        {"batting_team":[batting_team],"bowling_team":[bowling_team],"city":[city],"current_socre":[current_socre],
         "balls_left":[balls_left],"wickets_left":[wickets_left],"crr":[crr],"last_five":[last_five]})


    result = pipe.predict(input_df)
    st.text("Predicted Socre is : "+ str(int(result[0])))


    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )


    add_bg_from_local('image/bg3.png')



