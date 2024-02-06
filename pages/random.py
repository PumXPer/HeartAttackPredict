import streamlit as st
import pandas as pd
import random

# Create an initial empty DataFrame
df_dict = {
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
    sex = random.choice(["0", "1"])
    cp = random.choice(["0", "1", "2", "3"])
    trtbps = random.randint(90, 200)
    chol = random.randint(100, 600)
    fbs = random.choice(["0", "1"])
    restecg = random.choice(["0", "1"])
    thalachh = random.randint(60, 200)
    exng = random.choice(["0", "1"])
    oldpeak = round(random.uniform(0.0, 6.2), 1)
    slp = random.choice(["0", "1", "2"])
    caa = random.randint(0, 3)
    thall = random.choice(["0", "1", "2"])

    # Update the DataFrame with the new values
    df_dict['Name'].append(name)
    df_dict['Age'].append(age)
    df_dict['Sex'].append(sex)
    df_dict['cp'].append(cp)
    df_dict['trtbps'].append(trtbps)
    df_dict['chol'].append(chol)
    df_dict['fbs'].append(fbs)
    df_dict['restecg'].append(restecg)
    df_dict['thalachh'].append(thalachh)
    df_dict['exng'].append(exng)
    df_dict['oldpeak'].append(oldpeak)
    df_dict['slp'].append(slp)
    df_dict['caa'].append(caa)
    df_dict['thall'].append(thall)

# Button to generate random values and update the DataFrame
if st.button('Generate Random Values'):
    generate_random_values()

# Display the DataFrame
df = pd.DataFrame(df_dict)

st.write(df)
