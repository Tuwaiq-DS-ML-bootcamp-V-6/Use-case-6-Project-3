import streamlit as st
import plotly.express as px
import pandas as pd
# Calculate the top 10 districts
df=pd.read_csv("realEstate.csv")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write("")
with col2:
    st.image('pic.png')
with col3:
    st.write("")
district_counts = df['district'].value_counts()
top_10_districts = district_counts.nlargest(10)
df_top_10 = df[df['district'].isin(top_10_districts.index)]

# Create the pie chart
st.write('Top 10 Districts by Number of Properties in Riyadh')
st.image("sec_pic.png")

st.image('thered.png')


