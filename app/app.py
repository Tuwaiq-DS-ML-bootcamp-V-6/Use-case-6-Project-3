import streamlit as st
import plotly.express as px
import body as b


def intro():
    st.html(
        """
            <script>
            // TO MAKE THE MAP APPEAR YOU MUST
    // ADD YOUR ACCESS TOKEN FROM
    // https://account.mapbox.com
    mapboxgl.accessToken = 'pk.eyJ1Ijoia2gtYWJvb2Q0OCIsImEiOiJjbHdjMXJxOW8wczQwMmlwbHMxemN6cnJ0In0.zKxvqAq44877yPUqTDx0nQ';
    const map = new mapboxgl.Map({
        container: 'map',
        // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [24.774265, 46.738586],
        zoom: 13
    });

    map.addControl(
        new MapboxDirections({
            accessToken: mapboxgl.accessToken
        }),
        'top-left'
    );
            </script>

            """,
    )

    st.html("""
            <style>
            body { margin: 0; padding: 0; }
            #map { position: absolute; top: 0; bottom: 0; width: 100%; }
            </style>
            """)

    st.html("""
            <div id="map"></div>
            """)

    st.title("Find Your New Home in Riyadh!")
    st.write("""
             When thinking about moving to Riyadh, imagine you're setting out on an exciting journey. Picture yourself guided by an old friend who knows the city well and is ready to share insights about the best places to live, whether it's a cozy apartment, a luxurious villa, or a perfect plot of land. Silly Belly absolutely got you covered with our insights.
    """)


def conclusion():
    st.header("THE END")


def sidebar(options):
    with st.form(key="Form1"):
        with st.sidebar:
            st.title("Let old Silly Belly help you")
            st.image("app/images/sillybelly.png")

            options["select_type"] = st.sidebar.radio(
                "What kind of property are looking for?",
                ("Silly Belly's story", "Lands", "Apartments", "Villas"),
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
