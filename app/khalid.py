import streamlit as st
from streamlit import components


def main():
    map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>Mapbox Directions</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <script src="https://api.mapbox.com/mapbox-gl-js/v2.8.1/mapbox-gl.js"></script>
        <link href="https://api.mapbox.com/mapbox-gl-js/v2.8.1/mapbox-gl.css" rel="stylesheet" />
        <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.1/mapbox-gl-directions.js"></script>
        <link
            rel="stylesheet"
            href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.1/mapbox-gl-directions.css"
            type="text/css"
        />
        <style>
            body { margin: 0; padding: 0; }
            #map { position: absolute; top: 0; bottom: 0; width: 100%; height: 100%; }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            mapboxgl.accessToken = 'pk.eyJ1Ijoia2gtYWJvb2Q0OCIsImEiOiJjbHdjMXJxOW8wczQwMmlwbHMxemN6cnJ0In0.zKxvqAq44877yPUqTDx0nQ';
            const map = new mapboxgl.Map({
                container: 'map',
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
    </body>
    </html>
    """

    # Use streamlit.components.v1.html to display the map
    # components.v1.html(map_html, height=600)
