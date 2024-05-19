import streamlit as st
import plotly.express as px
import body as b


def intro():
    st.title("Find Your New Home in Riyadh!")
    st.write("""
             When thinking about moving to Riyadh, imagine you're setting out on an exciting journey. Picture yourself guided by an old friend who knows the city well and is ready to share insights about the best places to live, whether it's a cozy apartment, a luxurious villa, or a perfect plot of land. Silly Belly absolutely got you covered with his insights.
    """)


def conclusion():
    st.header("THE END")
    st.markdown(
        """
        With all his advice given, Silly Belly closed his eyes and said... 
        
        'Nighty night!' Sleep tight, and happy house hunting!
        
        """
    )


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

    col1, col2, col3 = st.columns([0.2, 5, 0.2])
    col2.image("app/images/sillybelly-house.png", use_column_width=True)
    sidebar(options)
    # st.write(options)
    intro()
    # st.write(type(options["select_type"]))
    b.body(options["select_type"])
    conclusion()


if __name__ == "__main__":
    main()
