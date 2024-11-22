# import libraries 

import streamlit as st

import eda

import predict

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('eda', 'predictor'))

if navigation == 'predictor':
    predict.run()

else :
    eda.run()

    

