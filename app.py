import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

st.title('Predictions Heart Attack')

tab1, tab2 = st.tabs(["Form ", "Result"])

with tab1:

    st.header('Form Predictions Heart Attack')
    title = st.text_input('Name', 'Life of Brian')
    number = st.number_input('Insert a number', step=1)

    col1, col2 = st.columns(2)
    with col1:
        sex = st.radio(
            "Sex",
            ["Man ", "Woman"],)
    with col2:
        exng =  st.radio(
                "Exercise Induced Angina (exng)",
                ["Yes", "No"])
    #st.selectbox('Exercise Induced Angina (exng) - เจ็บหน้าอกจากการออกกำลังกาย', ["No", "Yes"])

with tab2:
    st.header('Result Predictions Heart Attack')
    col1, col2 ,col3= st.columns(3)
    with col1:
        st.write('Name :', title) 
        st.write('Exercise Induced Angina :', exng)
    with col2:
        st.write('Age :', str(number))
        
    with col3:
        st.write('Gender :', sex)


    # Prepare data
    def prepare_data():
        0 if exng == 'No' else 1

    # Prediction model

    model = joblib.load('knn_model.joblib')

    user_input = pd.DataFrame({
   
})
    
    # Use the model to make predictions based on user input
    prediction = model.predict(user_input)[0]
    
    # Display the prediction
    if prediction == 0:
        st.write('Prediction:', 'No Heart Attack')
    else:
        st.write('Prediction:', 'Heart Attack')
