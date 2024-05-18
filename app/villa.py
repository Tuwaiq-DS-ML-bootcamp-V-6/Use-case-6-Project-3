import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.markdown("**TEST**")

villas = pd.read_csv('/Users/aabdu/Desktop/DS-ML-bootcamp/Use-case-6-Project-3/Use-case-6-Project-3/cleaned/villas.csv')
villas.drop(villas[villas['الحي'] == ' '].index, inplace=True)


st.text('What is the distribution of properties based on their number of rooms (عدد الغرف)?')

fig = px.histogram(villas, x="عدد الغرف", title="Distribution of Number of Rooms")
st.plotly_chart(fig)


grouped_villas = villas.groupby(['عدد الغرف', 'عدد الحمامات']).size().reset_index(name='count')

# Creating the Plotly figure
fig = px.bar(grouped_villas, x='عدد الغرف', y='count', color='عدد الحمامات',
             title='عدد الغرف و الحمامات في منازل الرياض',
             labels={'عدد الغرف': 'عدد الغرف', 'count': 'العدد', 'عدد الحمامات': 'عدد الحمامات'})

fig.update_layout(barmode='stack')

# Creating the Streamlit app
st.title('Visualization of Villas in Riyadh')
st.plotly_chart(fig)





# amenities_counts = villas.iloc[:, 9:-1].sum().reset_index()
# amenities_counts.columns = ['Amenity', 'Count']

# st.title("Villa Amenities Chart")
# fig = px.bar(amenities_counts, x='Amenity', y='Count', title="Amenities in Villas")
# st.plotly_chart(fig)



amenities_counts = villas.iloc[:, 9:-1].sum().reset_index()
amenities_counts.columns = ['Amenity', 'Count']

# Plotting Pie Chart
st.title("Villa Amenities Pie Chart")
fig = px.pie(amenities_counts, values='Count', names='Amenity', title="Amenities in Villas")
st.plotly_chart(fig)



# Plotting Scatter Plot


neighborhood_avg_price = villas.groupby('الحي')[['السعر الاجمالي','المساحة']].median().reset_index()
st.title("Price vs Area of Villas in Riyadh")
fig = px.scatter(neighborhood_avg_price, x='المساحة', y='السعر الاجمالي', title="Price vs Area of Villas in Riyadh",
                 labels={'المساحة': 'Area (sq. m)', 'السعر الاجمالي': 'Price (SAR)'},
                 color='الحي',log_x=True, log_y=True)
st.plotly_chart(fig)


#last C
neighborhood_avg_price = villas.groupby('الحي')['السعر الاجمالي'].median().reset_index()

neighborhood_avg_price = neighborhood_avg_price.round()
neighborhood_avg_price = neighborhood_avg_price.sort_values(by='السعر الاجمالي', ascending=True).head(10)
# Plotting bar chart
st.title("Average Price of Villas in Each Neighborhood of Riyadh")
fig = px.bar(neighborhood_avg_price, x='الحي', y='السعر الاجمالي', 
             title="Average Price of Villas in Each Neighborhood of Riyadh",
             labels={'الحي': 'Neighborhood', 'السعر الاجمالي': 'Average Price (SAR)'})
st.plotly_chart(fig)

# Display average price for each neighborhood
st.write("Average Price for Each Neighborhood:")
st.write(neighborhood_avg_price.head(11))

