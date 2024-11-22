# import libraries

import pandas as pd
import numpy as np

# visualisasi
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# streamlit
import streamlit as st


def run():
    # membuat title
    st.title('Breast Cancer Analysis')
    st.write('This page contains breast cancer analysis')

    # memasukkan gambar
    st.image('https://www.dallascitynews.net/wp-content/uploads/2021/10/Oct-2021-Breast-Cancer-Awareness.jpg')


    # section dataframe
    st.write("## Exploratory Data Analysis")
    st.write("---")
    st.write("### Dataframe")

    data = pd.read_csv("Breast_Cancer.csv")

    # show dataframe
    st.dataframe(data, height=150)
    st.write("Insight: ")
    st.write('''
            This dataset contains medical information covering various factors that affect cancer patient survival,
            such as age, marital status, tumor stage, tumor size, and estrogen and progesterone status.
            The Status column is the primary target for predicting patient survival,
            which is based on data from other variables in the dataset.
            ''')

    # section plot
    st.write("### Proportions")
    # Menghitung jumlah untuk setiap status
    target_size = data['Status'].value_counts()

    # # Membuat pie chart
    fig, ax = plt.subplots(figsize=(2.5, 2.5))
    ax.pie(target_size, labels=target_size.index, autopct='%1.1f%%', startangle=25, textprops={'fontweight': 'bold'})

    # # Menambahkan judul
    ax.set_title('Class Proportions', fontsize=10, pad=10)
    ax.axis('equal') 

    # Menampilkan pie chart di Streamlit
    st.pyplot(fig)
        
    options = ['N Stage', 'Tumor Stage (T Stage)', '6th Stage']
    selected_option = st.selectbox('Select Visualization Based on:', options)

    # Membuat visualisasi berdasarkan opsi yang dipilih
    if selected_option == 'N Stage':
        st.write("### Distribution of Life Status Based on N Stage")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=data, x='N Stage', hue='Status', palette='viridis', ax=ax)
        ax.set_title('Distribution of Life Status Based on N Stage')
        ax.set_xlabel('N Stage')
        ax.set_ylabel('Number of Patients')
        ax.legend(title='Status')
        st.pyplot(fig)

    elif selected_option == 'Tumor Stage':
        st.write("### Distribution of Life Status Based on T Stage")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=data, x='T Stage ', hue='Status', palette='coolwarm', ax=ax)
        ax.set_title('Distribution of Life Status Based on T Stage')
        ax.set_xlabel('T Stage')
        ax.set_ylabel('Number of Patients')
        ax.legend(title='Status')
        st.pyplot(fig)

    elif selected_option == 'Clinical Stage':
        st.write("### Distribution of Life Status Based on Clinical Stage ")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(data=data, x='6th Stage', hue='Status', palette='Set1', ax=ax)
        ax.set_title('Distribution of Life Status Based on Clinical Stage')
        ax.set_xlabel('Stadium')
        ax.set_ylabel('Number of Patients')
        ax.legend(title='Status')
        st.pyplot(fig)

if __name__ == '__main__':
    run()