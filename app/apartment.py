import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

apartments = pd.read_csv('/Users/aabdu/Desktop/DS-ML-bootcamp/Use-case-6-Project-3/Use-case-6-Project-3/cleaned/Apartments2.csv')
def bars():




     apartments = pd.read_csv('/Users/aabdu/Desktop/DS-ML-bootcamp/Use-case-6-Project-3/Use-case-6-Project-3/cleaned/Apartments.csv')
     apartments['عمر العقار'] = pd.to_numeric(apartments['عمر العقار'], errors='coerce')

     st.title("Real Estate Data Analysis")

     uinput = st.selectbox(
     "???",
     ['عمر العقار', 'المساحة', "السعر الاجمالي"])
     #uinput= "المساحة"
     


     # Calculate the mean عمر العقار for each حي
     mean_age = apartments.groupby('الحي')[uinput].mean().sort_values().reset_index()

     # Create a Plotly bar chart
     fig_age = px.bar(mean_age, x='الحي', y=uinput, 
                    labels={'الحي': 'الحي', uinput: f'{uinput} (متوسط بالسنة)'}, 
                    title=f'الحي vs. متوسط {uinput}')

     # Streamlit application
     
     st.write("This application displays the average age of properties by neighborhood.")

     # Display the Plotly chart in Streamlit
     return fig_age
    
    

def bar_color():

    apartments['مؤثثة'] = apartments['مؤثثة'].astype(str)
    features_input = st.selectbox(
     "???",
     ['مطبخ', 'مدخل سيارة', "مصعد",'مؤثثة','عدد الصالات'])
    
    #{عدد الصالات}+{مؤثثة}
    apartments[features_input] = apartments[features_input].astype(str)

    # Count the number of properties per حي and مؤثثة
    counts = apartments.groupby(['الحي', features_input]).size().unstack(fill_value=0)

    # Compute the total count and sort by it
    counts['Total'] = counts.sum(axis=1)
    counts = counts.nlargest(10, 'Total').sort_values(by='Total', ascending=True)
    counts = counts.drop(columns='Total')

    # Create traces for each value of 'مؤثثة'
    trace_0 = go.Bar(
    y=counts.index,
    x=counts['0'],
    name=f'غير {features_input}',
    text=counts['0'],
    textposition='inside',
    orientation='h'
    )

    trace_1 = go.Bar(
            y=counts.index,
            x=counts['1'],
            name=f'{features_input}',
            text=counts['1'],
            textposition='inside',
            orientation='h'
        )

        # Create the figure
    fig = go.Figure(data=[trace_0, trace_1])

        # Update the layout
    fig.update_layout(
            barmode='stack',
            title=f'(الحي vs {features_input}) أفضل 10 أحياء حسب عدد الشقق',
            yaxis=dict(title='الحي'),
            xaxis=dict(title='Count'),
            hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
        )
    return fig 


def piechart():
    neighborhood_counts = apartments['الحي'].value_counts()
    sorted_neighborhoods = neighborhood_counts.sort_values(ascending=False).head(10)

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=sorted_neighborhoods.index, values=sorted_neighborhoods.values)])
    fig.update_layout(
        title='نسبة عروض الشقق لكل حي',
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        )
    )

   
    
       
    return fig


def main():
    #st.plotly_chart(bars())
   


    st.markdown('''
                **What are the key features about your new apartment building ?**''')
                
                
    st.plotly_chart(bars())
                
                
    st.markdown('''Silly Belly's Insight: Think like an old prospector: consider the price, age, and space. These are your tools for striking it rich in comfort.''')

                
    st.markdown('''**What are the key features about your new apartment?**''')
                
                
    st.plotly_chart(bar_color())
                
                
    st.markdown('''Silly Belly's Insight: Check for a kitchen, elevator, parking, and if it's furnished. These goodies turn a place into a cozy home.''')
                
    st.markdown('''**Where can I start from?**''')
                
                
    st.plotly_chart(piechart())
                
                
    st.markdown('''Silly Belly's Insight: Use a pie chart like a treasure map. It shows districts with the most offers, guiding you to the best areas.''')
                
    

main()

