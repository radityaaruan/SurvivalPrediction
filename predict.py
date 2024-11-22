# import libraries
import pandas as pd
import numpy as np
import streamlit as st

# load model
import pickle

with open ('best.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    # membuat title
    st.title('Breast Cancer Death Predictor')
    st.write('''        
            The program will be created to predict the survival of cancer patients.
            For patients who are predicted to have a higher risk of death,
            will be given some special treatments and support information so that they can get the best care.
            Meanwhile, for patients who are predicted to have a lower risk,
            this program will provide advice on treatments that can help maintain health conditions.
            ''')

    # memasukkan gambar
    st.image('https://www.dallascitynews.net/wp-content/uploads/2021/10/Oct-2021-Breast-Cancer-Awareness.jpg')



    with st.form(key='form parameters'):
        age = st.number_input('Age: ',max_value = 70, min_value = 29, value = 45 )
        race = st.selectbox('Race: ', ('White', 'Other', 'Black', 'White', 'Black'))
        maritalStatus = st.selectbox('Marital Status: ', ('Married', 'Divorced', 'Single ', 'Widowed', 'Separated'))
        tstage = st.selectbox('T Stage: ', ('T3', 'T2', 'T4', 'T1', 'T3'))
        nstage = st.selectbox('N Stage: ', ('N1', 'N3', 'N2', 'N1', 'N2'))
        sixthStage = st.selectbox('6th Stage: ', ('IIIA', 'IIIC', 'IIB', 'IIA', 'IIIB'))
        Differentiate = st.selectbox('Differentiate: ', ('Poorly differentiated', 'Moderately differentiated', 'Well differentiated', 'Undifferentiated', 'Poorly differentiated'))
        grade = st.selectbox('Grade: ', ('3', '2', '1', 'anaplastic; Grade IV', '2'))
        astage = st.selectbox('A Stage: ', ('Regional', 'Distant'))
        tumorSize = st.selectbox('Tumor Size: ', ('3', '2', '1', 'anaplastic; Grade IV', '2'))
        estrogenStatus = st.selectbox('Estrogen Status', ('Positive', 'Negative'))
        progesteroneStatus = st.selectbox('Progesterone Status', ('Positive', 'Negative'))
        regionalnodeExamined = st.number_input('Regional Node Examined: ',max_value = 62, min_value = 1, value = 30 )
        reginolnodePositive = st.number_input('Reginol Node Positive: ',max_value = 46, min_value = 1, value = 30 )
        survivalMonths = st.number_input('survivalMonths: ',max_value = 107, min_value = 1, value = 60 )

        submit = st.form_submit_button('Predict !!')

    data = {
        'Age': age,
        'Race': race,
        'Marital Status': maritalStatus,
        'T Stage': tstage,
        'N Stage': nstage,
        '6th Stage': sixthStage,
        'differentiate': Differentiate,
        'Grade': grade,
        'A Stage': astage,
        'Tumor Size': tumorSize,
        'Estrogen Status': estrogenStatus,
        'Progesterone Status': progesteroneStatus,
        'Regional Node Examined': regionalnodeExamined,
        'Reginol Node Positive': reginolnodePositive,
        'Survival Months': survivalMonths
    }
    df = pd.DataFrame([data])
    st.dataframe(df)

    if submit:
        Status = model.predict(df)
        if Status == 1:
            st.write("Status = Dead")

        else:
            st.write("Status = Alive")

if __name__ == '__main__':
    run()
