def show(df,result):
    html_code_diagram = f"""
    <head>
      <style>
        table {{
          width: 100%;
          border-collapse: collapse;
        }}
        table,
        th,
        td {{
          border: 1px solid black;
        }}
      </style>
    </head>
    <table>
      <tr>
        <td>
            Name : {df['Name'][0]}
        </td>
        <td>
            Age : {df['Age'][0]}
        </td>
        <td>
            Sex : {df['Sex'][0]}
        </td>
      </tr>
      <tr>
        <td>
            Exercise Induced Angina : {df['exng'][0]}
        </td>
        <td>
            Oldpeak : {df['oldpeak'][0]}
        </td>
        <td>
            Cholesterol : {df['chol'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr>
        <td>
            Thalassemia : {df['thall'][0]}
        </td>
        <td>
            Resting Blood Pressure : {df['trtbps'][0]}
        </td>
      </tr>
      <tr>
        <td>
            Maximum Heart Rate Achieved : {df['thalachh'][0]}
        </td>
        <td>
            Fasting Blood Sugar > 120 mg/dl (fbs) : {df['fbs'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr>
        <td>
            Chest Pain Type : {df['cp'][0]}
        </td>
      </tr>
      <tr>
        <td>
            Slope of the Peak Exercise ST Segment : {df['slp'][0]}
        </td>
      </tr>
      <tr>
        <td>
            Resting Electrocardiographic Results : {df['restecg'][0]}
        </td>
      </tr>
      <tr>
        <td>
            Number of major vessels (0-3) colored by flourosopy : {df['caa'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr>
        <td>
            Result : {result}
        </td>
      </tr>
     """
    return html_code_diagram