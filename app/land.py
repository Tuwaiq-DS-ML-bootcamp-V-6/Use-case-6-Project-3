import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

lands = pd.read_csv("app/data/lands.csv")


def bar_color():
    uinput = st.selectbox("How do you prefer your land?", ["الغرض", "الواجهة"])
    lands["الحي"] = lands["الحي"].astype(str)
    lands[uinput] = lands[uinput].astype(str)

    # Temporary DataFrame to avoid multi-index issues
    temp = lands[["الحي", uinput]].copy()
    temp.columns = ["dis", "per"]

    # Count the number of properties per حي and الغرض
    counts = temp.groupby(["dis", "per"]).size().unstack(fill_value=0)

    # Compute the total count and sort by it
    counts["Total"] = counts.sum(axis=1)
    counts = counts.nlargest(10, "Total").sort_values(by="Total", ascending=True)
    counts = counts.drop(columns="Total")

    # Create traces for each value of 'الغرض'
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

    # Streamlit rendering

    # st.plotly_chart(fig)
    return fig


def bar():
    uinput = st.selectbox(
        "What is the general distribution of land offers across different neighborhoods?",
        ["المساحة", "سعر المتر"],
    )
    lands["الحي"] = lands["الحي"].astype(str)
    lands["المساحة"] = lands["المساحة"].astype(float)

    # Prepare the data for plotting
    temp = lands[["الحي", uinput]].copy()
    temp.columns = ["dis", "target"]

    mean_area = (
        temp.groupby("dis")["target"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )

    # Create the plot
    fig = px.bar(
        mean_area,
        x="dis",
        y="target",
        labels={"dis": "الحي", "target": uinput},
        title=f"الحي vs. {uinput}",
    )

    return fig


def pie():
    neighborhood_counts = lands["الحي"].value_counts()

    # Sort the neighborhoods and get the top 10
    sorted_neighborhoods = neighborhood_counts.sort_values(ascending=False).head(10)

    # Create the pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=sorted_neighborhoods.index, values=sorted_neighborhoods.values
            )
        ]
    )

    fig.update_layout(
        title="نسبة عروض الأراضي لكل حي",
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )

    # Display the chart
    return fig


def main():
    st.markdown("**What should you look for in a plot of land?**")
    st.plotly_chart(bar_color())
    st.markdown(
        "**Silly Belly's Insight:** Well, partner, when it comes to land, think about how you want it. Is it residential, commercial, or agricultural? Each type has its own charm and use. Pick what suits your dream best."
    )
    st.divider()
    st.plotly_chart(bar())
    st.markdown(
        "**Silly Belly's Insight:** Location, location, location! A prime spot means you're close to schools, markets, and transport. It’s like having the best seat at the rodeo—everything’s within reach, and the value can shoot up over time."
    )
    st.divider()
    st.markdown("""**Where can I start from?**""")
    st.plotly_chart(pie())
    st.markdown(
        "**Silly Belly's Insight:** To get your boots on the ground, start with a pie chart. This little beauty shows you which districts have the most offers. It's like a treasure map, guiding you to where the land opportunities are hottest."
    )


main()
# feel free to edit it
"""

The Land of Dreams:
What should you look for in a plot of land?
Insight: Look for plots in quiet neighborhoods with access to schools and markets. The land is the canvas where you'll build your dreams.

Why is the location of the land important?
Insight: A well-located plot ensures convenience and potential appreciation in value. Proximity to amenities like schools, markets, and transportation can significantly enhance the quality of life.

How does the size of the plot affect your future plans?
Insight: The size of the plot dictates the scope of your future home. Larger plots offer more flexibility in design and landscaping, while smaller plots may require more efficient use of space.

What amenities should you consider for your plot?
Input: [Select desired amenities]
Insight: Consider amenities like access to utilities, road frontage, and proximity to community services. These factors can greatly influence the practicality and future value of your land.

"""
