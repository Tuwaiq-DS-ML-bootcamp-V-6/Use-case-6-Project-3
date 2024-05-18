import streamlit as st
import apartment
import villa
import land


def body():
    st.header("The Land of Dreams")
    villa.main()
    st.header("The Villa of Comfort")
    land.main()
    st.header("The Cozy Apartment")
    apartment.main()
