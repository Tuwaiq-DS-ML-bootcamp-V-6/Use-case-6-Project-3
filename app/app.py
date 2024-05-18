import streamlit as st
import plotly.express as px
import body as b


def intro():
    st.title("Find Your New Home in Riyadh!")
    st.write("""
             When thinking about moving to Riyadh, imagine you're setting out on an exciting journey. Picture yourself guided by an old friend who knows the city well and is ready to share insights about the best places to live, whether it's a cozy apartment, a luxurious villa, or a perfect plot of land. Silly Belly absolutely got you covered with our insights.
    """)


from urllib.request import urlopen
import json


def body():
    # with urlopen(
    #     "https://raw.githubusercontent.com/Alnasser0/Saudi_Arabia-GeoJSON/master/SAU-geo.json"
    # ) as response:
    #     counties = json.load(response)
    #     fig = px.choropleth(
    #         geojson=counties,
    #         range_color=(0, 12),
    #     )
    #     fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #     fig.show()

    b.body()


def conclusion():
    st.header("THE END")


def sidebar(options):
    with st.form(key="Form1"):
        with st.sidebar:
            st.title("Let old Silly Belly help you")
            st.image("E:/Dev/Work/Tuwaiq/Use-case-6-Project-3/app/image.png")

            options["select_type"] = st.sidebar.radio(
                "What kind of property are looking for?",
                ("Silly Belly's story", "Lands", "Apartments", "Villas"),
            )


def main():
    options = {}
    sidebar(options)
    intro()
    body()
    conclusion()


if __name__ == "__main__":
    main()
