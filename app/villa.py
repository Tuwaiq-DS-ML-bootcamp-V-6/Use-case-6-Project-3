import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

villas = pd.read_csv("app/data/villas.csv")
villas.drop(villas[villas["الحي"] == " "].index, inplace=True)


def bar_color():
    uinput = st.selectbox(
        "How many rooms and bathrooms do villas in Riyadh typically have?",
        ["عدد الغرف", "عدد الصالات", "عدد الحمامات"],
    )
    villas["الحي"] = villas["الحي"].astype(str)
    villas[uinput] = villas[uinput].astype(str)

    # Temporary DataFrame to avoid multi-index issues
    temp = villas[["الحي", uinput]].copy()
    temp.columns = ["dis", "per"]

    # Count the number of properties per حي and عدد الغرف
    counts = temp.groupby(["dis", "per"]).size().unstack(fill_value=0)

    # Compute the total count and sort by it
    counts["Total"] = counts.sum(axis=1)
    counts = counts.nlargest(10, "Total").sort_values(by="Total", ascending=True)
    counts = counts.drop(columns="Total")

    # Create traces for each value of uinput
    traces = []
    for purpose in counts.columns:
        traces.append(
            go.Bar(
                y=counts.index,
                x=counts[purpose],
                name=purpose,
                text=counts[purpose],
                textposition="inside",
                orientation="h",
            )
        )

    # Create the figure
    fig = go.Figure(data=traces)

    # Update the layout
    fig.update_layout(
        barmode="stack",
        title=f"(الحي vs {uinput}) أفضل 10 أحياء حسب عدد العقارات",
        yaxis=dict(title="الحي"),
        xaxis=dict(title="Count"),
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )

    # Show the figure

    return fig


def bars():
    uinput = st.selectbox(
        "What is the typical size of villas in different neighborhoods?",
        ["المساحة", "السعر الاجمالي"],
    )
    mean_area = villas.groupby("الحي")[uinput].mean().sort_values().reset_index()

    # Plot
    fig = px.bar(
        mean_area,
        x=uinput,
        y="الحي",
        labels={"الحي": "الحي", uinput: f"{uinput} (متوسط بالمتر المربع)"},
        title=f"الحي vs. متوسط {uinput}",
    )

    # Streamlit UI
    st.title(f"توزيع {uinput} في الأحياء")

    return fig


def bar_color2():
    uinput = st.selectbox(
        "What amenities should you expect in a villa?",
        ["درج صالة", "مطبخ", "غرفة خادمة", "غرفة سائق", "ملحق", "حوش", "مسبح", "قبو"],
    )
    villas[uinput] = villas[uinput].astype(str)

    # Count the number of properties per حي and مطبخ
    counts = villas.groupby(["الحي", uinput]).size().unstack(fill_value=0)

    # Compute the total count and sort by it
    counts["Total"] = counts.sum(axis=1)
    counts = counts.nlargest(10, "Total").sort_values(by="Total", ascending=True)
    counts = counts.drop(columns="Total")

    # Create traces for each value of uinput
    trace_0 = go.Bar(
        y=counts.index,
        x=counts["0"],
        name=f" بدون {uinput}  ",
        text=counts["0"],
        textposition="inside",
        orientation="h",
    )

    trace_1 = go.Bar(
        y=counts.index,
        x=counts["1"],
        name=f"{uinput}",
        text=counts["1"],
        textposition="inside",
        orientation="h",
    )

    # Create the figure
    fig = go.Figure(data=[trace_0, trace_1])

    # Update the layout
    fig.update_layout(
        barmode="stack",
        title=f"(الحي vs {uinput}) أفضل 10 أحياء حسب عدد العقارات",
        yaxis=dict(title="الحي"),
        xaxis=dict(title="Count"),
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )

    return fig


def main():
    st.plotly_chart(bar_color())
    st.markdown(
        "**Silly Belly's Insight:** Howdy! Villas in Riyadh come with different numbers of rooms and bathrooms. Whether you need space for a large family or a smaller household, there's a villa out there with the perfect setup for you."
    )
    st.divider()
    st.plotly_chart(bars())
    st.markdown(
        "**Silly Belly's Insight:** Size matters, partner! Villas come in all shapes and sizes. Check out the average sizes in different neighborhoods to find one that fits your needs. Some places offer sprawling spaces while others are more compact and cozy."
    )
    st.divider()
    st.plotly_chart(bar_color2())
    st.markdown(
        "**Silly Belly's Insight:** Look for the goodies! Many villas come with top-notch amenities like a maid's room, driver's room, annex, garden, swimming pool, basement, garage, and elevator. These features can turn a house into a luxurious home."
    )


main()
# st.text(
#     "What is the distribution of properties based on their number of rooms (عدد الغرف)?"
# )

# fig = px.histogram(villas, x="عدد الغرف", title="Distribution of Number of Rooms")
# st.plotly_chart(fig)


# grouped_villas = (
#     villas.groupby(["عدد الغرف", "عدد الحمامات"]).size().reset_index(name="count")
# )

# # Creating the Plotly figure
# fig = px.bar(
#     grouped_villas,
#     x="عدد الغرف",
#     y="count",
#     color="عدد الحمامات",
#     title="عدد الغرف و الحمامات في منازل الرياض",
#     labels={"عدد الغرف": "عدد الغرف", "count": "العدد", "عدد الحمامات": "عدد الحمامات"},
# )

# fig.update_layout(barmode="stack")

# # Creating the Streamlit app
# st.title("Visualization of Villas in Riyadh")
# st.plotly_chart(fig)


# # amenities_counts = villas.iloc[:, 9:-1].sum().reset_index()
# # amenities_counts.columns = ['Amenity', 'Count']

# # st.title("Villa Amenities Chart")
# # fig = px.bar(amenities_counts, x='Amenity', y='Count', title="Amenities in Villas")
# # st.plotly_chart(fig)


# amenities_counts = villas.iloc[:, 9:-1].sum().reset_index()
# amenities_counts.columns = ["Amenity", "Count"]

# # Plotting Pie Chart
# st.title("Villa Amenities Pie Chart")
# fig = px.pie(
#     amenities_counts, values="Count", names="Amenity", title="Amenities in Villas"
# )
# st.plotly_chart(fig)


# # Plotting Scatter Plot


# neighborhood_avg_price = (
#     villas.groupby("الحي")[["السعر الاجمالي", "المساحة"]].median().reset_index()
# )
# st.title("Price vs Area of Villas in Riyadh")
# fig = px.scatter(
#     neighborhood_avg_price,
#     x="المساحة",
#     y="السعر الاجمالي",
#     title="Price vs Area of Villas in Riyadh",
#     labels={"المساحة": "Area (sq. m)", "السعر الاجمالي": "Price (SAR)"},
#     color="الحي",
#     log_x=True,
#     log_y=True,
# )
# st.plotly_chart(fig)


# # last C
# neighborhood_avg_price = villas.groupby("الحي")["السعر الاجمالي"].median().reset_index()

# neighborhood_avg_price = neighborhood_avg_price.round()
# neighborhood_avg_price = neighborhood_avg_price.sort_values(
#     by="السعر الاجمالي", ascending=True
# ).head(10)
# # Plotting bar chart
# st.title("Average Price of Villas in Each Neighborhood of Riyadh")
# fig = px.bar(
#     neighborhood_avg_price,
#     x="الحي",
#     y="السعر الاجمالي",
#     title="Average Price of Villas in Each Neighborhood of Riyadh",
#     labels={"الحي": "Neighborhood", "السعر الاجمالي": "Average Price (SAR)"},
# )
# st.plotly_chart(fig)

# # Display average price for each neighborhood
# st.write("Average Price for Each Neighborhood:")
# st.write(neighborhood_avg_price.head(11))
