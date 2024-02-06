import pickle
import streamlit as st
import pandas as pd
import random

from html_component import show

st.title('Predictions Heart Attack - Random Values')

# Create an initial empty DataFrame
data_json = {
    'Name': [],
    'Age': [],
    'Sex': [],
    'cp': [],
    'trtbps': [],
    'chol': [],
    'fbs': [],
    'restecg': [],
    'thalachh': [],
    'exng': [],
    'oldpeak': [],
    'slp': [],
    'caa': [],
    'thall': []
}

# Function to generate random values and update the DataFrame
def generate_random_values():
    name = "John Doe"  # You can replace this with a random name generation logic
    age = random.randint(18, 80)
    sex = random.choice(["Male", "Female"])
    cp = random.choice([
            "typical anigma (อาการแน่นหน้าอกทั่วไป)",
            "atypical anigma (แน่นหน้าอกผิดปกติ)",
            "non-anginal pain (อาการปวดแบบไม่เจ็บแน่นหน้าอก)",
            "asymptomatic (ไม่มีอาการ)",])
    trtbps = random.randint(90, 200)
    chol = random.randint(100, 600)
    fbs = random.choice(["Yes", "No"])
    restecg = random.choice([
            "Normal (ปกติ)",
            "There is an ST-T wave abnormality (มีความผิดปกติของคลื่น ST-T)",
            "Shows possible left ventricular hypertrophy (แสดงภาวะกระเป๋าหน้าท้องด้านซ้ายโตเกินที่เป็นไปได้)"
        ])
    thalachh = random.randint(60, 200)
    exng = random.choice(["Yes", "No"])
    oldpeak = round(random.uniform(0.0, 6.2), 1)
    slp = random.choice(["upsloping", "flat", "downsloping"])
    caa = random.randint(0, 3)
    thall = random.choice([
            "Normal (ปกติ)",
            "Fixed defect (เสียงเสีย)",
            "Reversable defect (เสียงกลับได้)"
        ])
    
    # Update the DataFrame with the new values
    data_json['Name'].append(name)
    data_json['Age'].append(age)
    data_json['Sex'].append(sex)
    data_json['cp'].append(cp)
    data_json['trtbps'].append(trtbps)
    data_json['chol'].append(chol)
    data_json['fbs'].append(fbs)
    data_json['restecg'].append(restecg)
    data_json['thalachh'].append(thalachh)
    data_json['exng'].append(exng)
    data_json['oldpeak'].append(oldpeak)
    data_json['slp'].append(slp)
    data_json['caa'].append(caa)
    data_json['thall'].append(thall)

    return data_json

def convert(df):
    df['exng'] = df['exng'].apply(lambda x: 0 if x == 'No' else 1)
    df['cp'] = df['cp'].map({
        'typical anigma (อาการแน่นหน้าอกทั่วไป)': 0,
        'atypical anigma (แน่นหน้าอกผิดปกติ)': 1,
        'non-anginal pain (อาการปวดแบบไม่เจ็บแน่นหน้าอก)': 2,
        'asymptomatic (ไม่มีอาการ)': 3
    })
    df['fbs'] = df['fbs'].apply(lambda x: 0 if x == 'No' else 1)
    df['restecg'] = df['restecg'].map({
        'Normal (ปกติ)': 0,
        'There is an ST-T wave abnormality (มีความผิดปกติของคลื่น ST-T)': 1,
        'Shows possible left ventricular hypertrophy (แสดงภาวะกระเป๋าหน้าท้องด้านซ้ายโตเกินที่เป็นไปได้)': 2
    })
    df['slp'] = df['slp'].map({
        'upsloping': 0,
        'flat (horizontal)': 1,
        'downsloping': 2
    })
    df['thall'] = df['thall'].map({
        'Normal (ปกติ)': 0,
        'Fixed defect (เสียงเสีย)': 1,
        'Reversable defect (เสียงกลับได้)': 2
    })

    col_drop = ['Name', 'Age','Sex']
    df = df.drop(col_drop, axis=1)


    return df


# Button to generate random values and update the DataFrame
if st.button('Generate Random Values'):
    data_json = generate_random_values()

try:
    # Display the DataFrame
    df = pd.DataFrame(data_json)

    # st.write(df)
    # Applying the convert function to the DataFrame
    df_pred = convert(df)

    # st.write(df_pred)

    model = pickle.load(open('models/lr_model.pkl', 'rb'))

    x = df_pred.values.tolist()

    prediction = model.predict(x)
        
    # Display the prediction
    if prediction == 0:
        result = 'No Heart Attack'
    else:
        result = 'Heart Attack'

    st.markdown(show(data_json,result),unsafe_allow_html=True)

except:
    st.warning('Please click the button to generate random values')
