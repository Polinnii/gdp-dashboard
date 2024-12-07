import streamlit as st
import pandas as pd
import plotly.express as px


file_name = 'data/Pokemon.csv'
df = pd.read_csv(file_name)

with st.sidebar:
    option_1 = st.selectbox('x_param',df.columns)
    option_2 = st.selectbox('y_param',df.columns)
    option_3 = st.selectbox('z_param',df.columns)
    option_4 = st.selectbox('color',df.columns)

x = option_1
y = option_2
z = option_3

fig = px.scatter_3d(df, x=x, y=y, z=z, color=option_4)
st.plotly_chart(fig)
