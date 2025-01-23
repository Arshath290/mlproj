import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import os


model = joblib.load('final_model.pkl')


# Function for making predictions
def make_prediction(features):
    return model.predict([features])
   
# Streamlit App UI
st.title('Resale Price Prediction')

# Numerical Input Fields
floor_area = st.number_input('Floor Area (sqm)', min_value=0.0, max_value=500.0, value=100.0)
remaining_lease_years = st.number_input('Remaining Lease Years', min_value=0, max_value=100, value=60)

# Categorical Dropdown Boxes
town_options = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH',
                'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG',
                'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN']
town = st.selectbox('Town', town_options)

flat_type_options = ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION']
flat_type = st.selectbox('Flat Type', flat_type_options)

storey_range_options = ['01 TO 03', '04 TO 06', '07 TO 09', '10 TO 12', '13 TO 15', '16 TO 18', '19 TO 21', 
                        '22 TO 24', '25 TO 27', '28 TO 30', '31 TO 33', '34 TO 36', '37 TO 39', '40 TO 42', 
                        '43 TO 45', '46 TO 48', '49 TO 51']
storey_range = st.selectbox('Storey Range', storey_range_options)

distance_from_expressway_options = ['101-150m', '151-300m', '301-500m', '51-100m', '<=50m', '>500m']
distance_from_expressway = st.selectbox('Distance from Expressway', distance_from_expressway_options)

# Make prediction when the button is clicked
if st.button('Predict'):
    # Create a list of features based on the user's input
    features = [floor_area, remaining_lease_years]

    # Encode categorical columns
    def encode_column(options, selected_value):
        return [1 if option == selected_value else 0 for option in options]

    features.extend(encode_column(town_options, town))
    features.extend(encode_column(flat_type_options, flat_type))
    features.extend(encode_column(storey_range_options, storey_range))
    features.extend(encode_column(distance_from_expressway_options, distance_from_expressway))

    # Make prediction
    prediction = make_prediction(features)
    st.write(f"The predicted resale price is: ${prediction[0]:,.2f}")
