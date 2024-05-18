import streamlit as st
import apartment
import villa
import land


def body(target: str) -> None:
    match target:
        case "Lands":
            st.header("The Land of Dreams")
            land.main()

        case "Villas":
            st.header("The Villa of Comfort")
            villa.main()

        case "Apartments":
            st.header("The Cozy Apartment")
            apartment.main()
        case _:
            st.header("The Land of Dreams")
            land.main()
