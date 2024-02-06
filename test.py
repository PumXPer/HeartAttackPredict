import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model using pickle
with open('your_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Streamlit app
st.title('Heart Disease Prediction App')

# Sidebar for user input
st.sidebar.header('User Input')
cp = st.sidebar.selectbox('Chest Pain Type (cp)', [0, 1, 2, 3])
trtbps = st.sidebar.slider('Resting Blood Pressure (trtbps)', 90, 200, 120)
chol = st.sidebar.slider('Cholesterol (chol)', 100, 600, 200)
fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', [0, 1])
restecg = st.sidebar.selectbox('Resting Electrocardiographic Results (restecg)', [0, 1, 2])
thalachh = st.sidebar.slider('Maximum Heart Rate Achieved (thalachh)', 60, 200, 150)
exng = st.sidebar.selectbox('Exercise Induced Angina (exng)', [0, 1])
oldpeak = st.sidebar.slider('Oldpeak (ST depression induced by exercise relative to rest)', 0.0, 6.2, 1.0)
slp = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment (slp)', [0, 1, 2])
caa = st.sidebar.slider('Number of Major Vessels Colored by Flouroscopy (caa)', 0, 4, 0)
thall = st.sidebar.selectbox('Thalassemia (thall)', [1, 2, 3])

# Create a DataFrame with user inputs
user_input = pd.DataFrame({
    'cp': [cp],
    'trtbps': [trtbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalachh': [thalachh],
    'exng': [exng],
    'oldpeak': [oldpeak],
    'slp': [slp],
    'caa': [caa],
    'thall': [thall]
})

# Main content area
if st.button('Make Prediction'):
    # Use the model to make predictions based on user input
    prediction = model.predict(user_input)[0]
    
    # Display the prediction
    st.write('Prediction:', prediction)
