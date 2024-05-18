import streamlit as st


def main():
    st.write("khalid")
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
