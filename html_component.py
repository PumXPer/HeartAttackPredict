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
    <div style="margin-top: 10px;"></div>
    <table>
      <tr style="background-color:  rgb(78, 77, 75)">
        <td style="width: 20%">
            <b>Name</b> : 
        </td>
        <td>
            {df['Name'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Age</b>:
        </td>
        <td>
            {df['Age'][0]}
        </td>
        <td>
            <b>Sex</b>:
        </td>
         <td>
            {df['Sex'][0]}
        </td>
      </tr>
      <tr style="background-color:  rgb(78, 77, 75)">
       <td>
            <b>Oldpeak</b> : 
        </td>
        <td>
            {df['oldpeak'][0]}
        </td>
        <td>
            <b>Cholesterol</b> :
        </td>
        <td>
            {df['chol'][0]}
        </td>
      </tr>
       <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Exercise Induced Angina</b> :
        </td>
        <td>
            {df['exng'][0]}
        </td>
        <td>
            <b>Thalassemia</b> : 
        </td>
        <td>
            {df['thall'][0]}
        </td>
      </tr>
       <tr style="background-color:  rgb(78, 77, 75)">
        <td>
            <b>Resting Blood Pressure</b> :
        </td>
        <td>
            {df['trtbps'][0]}
        </td>
        <td>
            <b>Maximum Heart Rate Achieved</b> :
        </td>
        <td>
            {df['thalachh'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Fasting Blood Sugar > 120 mg/dl (fbs)</b> :
        </td>
        <td>
            {df['fbs'][0]}
        </td>
      <tr style="background-color:  rgb(78, 77, 75)">
        <td>
            <b>Chest Pain Type</b> : 
        </td>
        <td>
            {df['cp'][0]}
        </td>
      </tr>
      <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Slope of the Peak Exercise ST Segment</b> :
        </td>
         <td>
            {df['slp'][0]}
        </td>
      </tr>
      <tr style="background-color:  rgb(78, 77, 75)">
        <td>
            <b>Resting Electrocardiographic Results</b> :
        </td>
         <td>
            {df['restecg'][0]}
        </td>
      </tr>
      <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Number of major vessels (0-3) colored by flourosopy</b> :
        </td>
        <td>
            {df['caa'][0]}
        </td>
      </tr>
      <tr style="background-color:  rgb(108, 106, 103)">
        <td>
            <b>Slope of the Peak Exercise ST Segment</b> :
        </td>
        <td>
            {df['slp'][0]}
        </td>
      </tr>
    </table>
    <table>
      <tr style="background-color:  rgb(86, 72, 52)">
        <td>
            <b>Result</b> : {result}
        </td>
      </tr>
     """
    return html_code_diagram