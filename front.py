import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(page_title = "Hackatoon 2022 BBVA",page_icon=":bar_chart:",layout="wide")
st.title('A++ Hackaton BBVA - 2022')


#--------CARGA DE DATOS--------
df = pd.read_excel('FirstProject\output.xlsx',nrows= 100)
st.dataframe(df)


#-----SIDEBAR SECCION-----------
st.sidebar.header("Filtra aqui.")
calle1 = st.sidebar.multiselect("Selecciona la calle1",options=df['EntreCalle1'].unique(),default=df['EntreCalle1'].unique())