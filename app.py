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
st.markdown("Despite the challenges of finding a suitable apartment, there are steps you can take to find one in Riyadh at a reasonable price.Upon receiving a job opportunity in Riyadh, I began searching for suitable accommodation. During my search, I came across a dataset that illustrated the factors influencing the decision to rent.Firstly, we looked into which neighborhoods have the highest demand for rental apartments. Through the dataset, it became clear which neighborhoods are available for rent.")

district_counts = df['district'].value_counts()
top_10_districts = district_counts.nlargest(10)
df_top_10 = df[df['district'].isin(top_10_districts.index)]

# Create the pie chart
st.write('Top 10 Districts by Number of Properties in Riyadh')
st.image("sec_pic.png")
st.markdown("Through this exploration, we discovered that the age of the property impacts the price. Generally, older properties tend to have lower rental prices.")
st.image('thered.png')


