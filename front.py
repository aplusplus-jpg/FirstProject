import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(page_title = "Hackatoon 2022 BBVA",page_icon=":bar_chart:",layout="wide")
st.title('A++ Hackaton BBVA - 2022')

st.file_uploader("Please, upload your csv")
#st.button("Read a dataset (.csv)", on_click=)

#--------CARGA DE DATOS--------
#df = pd.read_excel('dataset/output.xlsx',nrows= 100)
df = pd.read_csv('dataset/Final_Data_Hackathon_2022.csv')
st.dataframe(df[0:5])

for fila in df.iterrows():
    st.text_area(fila)


#-----SIDEBAR SECCION-----------
st.sidebar.header("Filtra aqui.")
calle1 = st.sidebar.multiselect("Selecciona la calle1",options=df['EntreCalle1'].unique(),default=df['EntreCalle1'].unique())