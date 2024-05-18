import streamlit as st
import plotly.express as px
import body as b
import khalid


def intro():
    st.title("Find Your New Home in Riyadh!")
    st.write("""
             When thinking about moving to Riyadh, imagine you're setting out on an exciting journey. Picture yourself guided by an old friend who knows the city well and is ready to share insights about the best places to live, whether it's a cozy apartment, a luxurious villa, or a perfect plot of land. Silly Belly absolutely got you covered with his insights.
    """)
    khalid.main()


def conclusion():
    st.header("THE END")


def sidebar(options):
    with st.form(key="Form1"):
        with st.sidebar:
            st.title("Let old Silly Belly help you")
            st.image("app/images/sillybelly.png")

            options["select_type"] = st.sidebar.radio(
                "What kind of property are looking for?",
                ("Lands", "Apartments", "Villas"),
            )


def main():
    options = {}
    sidebar(options)
    # st.write(options)
    intro()
    b.body()
    conclusion()


if __name__ == "__main__":
    main()
