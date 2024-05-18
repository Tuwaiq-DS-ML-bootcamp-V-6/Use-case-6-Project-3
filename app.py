import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image, ImageOps
import json
import requests 
from streamlit_lottie import st_lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

realestate = load_lottiefile("ani1.json")

st_lottie(realestate,key="real_estate")


# Calculate the top 10 districts
df=pd.read_csv("realEstate.csv")
st.markdown("What factors make the real estate market in Riyadh attractive to investors?The real estate market for apartments in Riyadh is considered one of the most important property markets in the Kingdom of Saudi Arabia for investors. Riyadh offers diverse and lucrative opportunities for investing in apartment properties, whether through purchasing and leasing apartments or developing new real estate projects.During our research, a set of data revealed the most suitable places for investment.Various areas in Riyadh cater to the needs of investors, ranging from upscale residential neighborhoods to industrial and commercial zones. Investors can achieve substantial returns on their investments in Riyadh's apartment market due to the strong demand for housing in the city.")

district_counts = df['district'].value_counts()
top_10_districts = district_counts.nlargest(10)
df_top_10 = df[df['district'].isin(top_10_districts.index)]

# Create the pie chart
st.write('Top 10 Districts by Number of Properties in Riyadh')

image_path = 'd.png'
image = Image.open(image_path)
frame_width = 2 
frame_color = (21, 60, 61)  
framed_image = ImageOps.expand(image, border=frame_width, fill=frame_color)
st.image(framed_image, use_column_width=True)








search = load_lottiefile("ani2.json")

st_lottie(search,key="search",width=200)


st.markdown("Through this exploration, we discovered that the age of the property impacts the price. Generally, older properties tend to have lower rental prices.")
image_path = 'image copy.png'
image = Image.open(image_path)
frame_width = 2 
frame_color = (21, 60, 61)  
framed_image = ImageOps.expand(image, border=frame_width, fill=frame_color)
st.image(framed_image, use_column_width=True)




st.markdown("From our analysis, we found that an increase in the number of bathrooms is associated with an increase in the apartment size. However, this leads to a significant rise in prices, making them less attractive to buyers and investors. Therefore, investing in moderately sized apartments with a reasonable number of bathrooms can be more effective in attracting buyers and ensuring a quicker return on investment.")

image_path = 'image.png'
image = Image.open(image_path)
frame_width = 2 
frame_color = (21, 60, 61)  
framed_image = ImageOps.expand(image, border=frame_width, fill=frame_color)
st.image(framed_image, use_column_width=True)


st.markdown("In Riyadh's real estate market, the presence of kitchens and air conditioning systems holds immense sway over investor interest. These features not only enhance tenant satisfaction but also underscore the property's value and desirability, making it an attractive investment opportunity.")

image_path = 's.png'
image = Image.open(image_path)
frame_width = 2 
frame_color = (21, 60, 61)  
framed_image = ImageOps.expand(image, border=frame_width, fill=frame_color)
st.image(framed_image, use_column_width=True)

st.markdown("In conclusion, the real estate market for apartments in Riyadh offers highly promising and attractive investment opportunities. The diversity of the city's neighborhoods, ranging from upscale residential areas to industrial and commercial zones, provides a wide array of investment options that cater to various preferences and strategies. If you are looking for an investment that yields tangible and quick returns, the apartment market in Riyadh is the perfect destination. Don't miss the opportunity to join the thriving momentum in this dynamic and promising market!")


