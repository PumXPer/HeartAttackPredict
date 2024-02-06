import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model using pickle
with open('lr_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Streamlit app
st.title('Heart Disease Prediction App')

# Create a DataFrame with user inputs
user_input = pd.DataFrame({
    'cp': [1],
    'trtbps': [130],
    'chol': [250],
    'fbs': [0],
    'restecg': [1],
    'thalachh': [150],
    'exng': [0],
    'oldpeak': [2.5],
    'slp': [2],
    'caa': [1],
    'thall': [3],
})

# Main content area
if st.button('Make Prediction'):
    # Use the model to make predictions based on user input
    prediction = model.predict(user_input)[0]
    
    # Display the prediction
    st.write('Prediction:', prediction)
