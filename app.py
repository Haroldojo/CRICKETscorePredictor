import streamlit as st
import pickle
import pandas as pd

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Define teams and cities
teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 
    'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 
    'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 
    'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 
    'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 
    'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 
    'Christchurch', 'Trinidad'
]

st.title("Cricket Score Predictor")

# Input fields
batting_team = st.selectbox("Select the batting team", sorted(teams))
bowling_team = st.selectbox("Select the bowling team", sorted(teams))
city = st.selectbox("Select the city", sorted(cities))
current_score = st.number_input("Current Score", min_value=0, value=100)
overs = st.number_input("Overs Completed", min_value=0.0, max_value=50.0, value=10.0)
wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=2)
last_five = st.number_input("Runs Scored in Last Five Overs", min_value=0, value=30)

if st.button("Predict Score"):
    ball_left = 120 - (overs * 6)
    wicket_left = 10 - wickets
    current_run_rate = current_score / overs

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 
         'current_score': [current_score], 'ball_left': [ball_left], 
         'wicket_left': [wicket_left], 'current_run_rate': [current_run_rate], 
         'last_five': [last_five]}
    )

    result = pipe.predict(input_df)
    prediction = int(result[0])

    st.write(f"Predicted Score: {prediction}")

