import streamlit as st
import pandas as pd
import joblib
import pickle
from html_component import *

st.title('Predictions Heart Attack')

tab1, tab2 = st.tabs(["Form ", "Result"])

with tab1:

    st.header('Form Predictions Heart Attack')
    name = st.text_input('Name', 'Life of Brian')
    age = st.number_input('Age',min_value=0,value=30, step=1)

    col1, col2 = st.columns(2)
    with col1:
        sex = st.radio(
            "Sex",
            ["Man ", "Woman"],)
        caa = st.number_input('Number of major vessels (0-3) colored by flourosopy', min_value=0, max_value=3, step=1)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', ["Yes", "No"])
        slp = st.selectbox('Slope of the Peak Exercise ST Segment (slp)', [
            "upsloping", 
            "flat (horizontal)" , 
            "downsloping"
        ])
    with col2:
        exng =  st.radio(
                "Exercise Induced Angina (exng)",
                ["Yes", "No"])
        cp = st.selectbox('Chest Pain Type (cp)', [
            "typical anigma (อาการแน่นหน้าอกทั่วไป)",
            "atypical anigma (แน่นหน้าอกผิดปกติ)",
            "non-anginal pain (อาการปวดแบบไม่เจ็บแน่นหน้าอก)",
            "asymptomatic (ไม่มีอาการ)",])
        restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', [
            "Normal (ปกติ)",
            "There is an ST-T wave abnormality (มีความผิดปกติของคลื่น ST-T)",
            "Shows possible left ventricular hypertrophy (แสดงภาวะกระเป๋าหน้าท้องด้านซ้ายโตเกินที่เป็นไปได้)"
        ])
        thall = st.selectbox('Thalassemia (thall)', [
            "Normal (ปกติ)",
            "Fixed defect (เสียงเสีย)",
            "Reversable defect (เสียงกลับได้)"
        ])

    trtbps = st.slider('Resting Blood Pressure (trtbps)', 90, 200, 120)
    chol = st.slider('Cholesterol (chol)', 100, 600, 200)
    thalachh = st.slider('Maximum Heart Rate Achieved (thalachh)', 60, 200, 150)
    oldpeak = st.slider('Oldpeak (ST depression induced by exercise relative to rest)', 0.0, 6.2, 1.0)
    
    
    #st.selectbox('Exercise Induced Angina (exng) - เจ็บหน้าอกจากการออกกำลังกาย', ["No", "Yes"])

with tab2:
    st.header('Result Predictions Heart Attack')
    # col1, col2 ,col3= st.columns(3)
    # with col1:
    #     st.write('Name :', name) 
    #     st.write('Exercise Induced Angina :', exng)
    #     st.write('Thalassemia :', thall)
    # with col2:
    #     st.write('Age :', str(age))
    #     st.write('Oldpeak :', oldpeak)
    #     st.write('Resting Blood Pressure :', trtbps)
    # with col3:
    #     st.write('Gender :', sex)
    #     st.write('Cholesterol :', chol)
        
    
    # col4, col5 = st.columns(2)
    # with col4:
    #     st.write('Maximum Heart Rate Achieved :', thalachh)
        
    # with col5:
    #     st.write('Fasting Blood Sugar > 120 mg/dl (fbs) :', fbs)
        
    # st.write('Chest Pain Type :', cp)
    # st.write('Slope of the Peak Exercise ST Segment :', slp)
    # st.write('Resting Electrocardiographic Results :', restecg)
    # st.write('Number of major vessels (0-3) colored by flourosopy :', caa)

    df_dict = {
        'Name' : [name],
        'Age' : [age],
        'Sex' : [sex],
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
    }

    # st.write('Result :', df_dict)
    
    # Prepare data
    df =  pd.DataFrame(df_dict)

    # st.write(df)

    def prepare_data(df):
        df['exng'] = 0 if exng == 'No' else 1
        df['cp'] = 0 if cp == 'typical anigma (อาการแน่นหน้าอกทั่วไป)' else 1 if cp == 'atypical anigma (แน่นหน้าอกผิดปกติ)' else 2 if cp == 'non-anginal pain (อาการปวดแบบไม่เจ็บแน่นหน้าอก)' else 3
        df['fbs'] = 0 if fbs == 'No' else 1
        df['restecg'] = 0 if restecg == 'Normal (ปกติ)' else 1 if restecg == 'There is an ST-T wave abnormality (มีความผิดปกติของคลื่น ST-T)' else 2
        df['slp'] = 0 if slp == 'upsloping' else 1 if slp == 'flat (horizontal)' else 2
        df['thall'] = 0 if thall == 'Normal (ปกติ)' else 1 if thall == 'Fixed defect (เสียงเสีย)' else 2

        col_drop = ['Name', 'Age','Sex']
        df = df.drop(col_drop, axis=1)

        return df

    # Prediction model

    # model = joblib.load('knn_model.joblib')

    with open('knn_model.pkl', 'rb') as file:
        model = pickle.load(file)

    user_input = prepare_data(df)
    
    # Use the model to make predictions based on user input
    prediction = model.predict(user_input)[0]
    
    # Display the prediction
    if prediction == 0:
        result = 'No Heart Attack'
    else:
        result = 'Heart Attack'

    st.markdown(show(df_dict,result),unsafe_allow_html=True)
