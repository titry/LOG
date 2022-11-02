import streamlit as st
import utils as utl
from views import home, gallery, daily

def navigation():
    route = utl.get_current_route()
    if route == "HOME":
        home.load_view()
    elif route == "GALLERY":
        gallery.load_view()
    elif route == "DAILY":
        daily.load_view()
    
    #no use
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()

def initialize():
    if "initialized" in st.session_state:
        return
    st.session_state.initialized = True


def main():
    initialize()

    navigation()
    st.markdown(
        """
        <style>
        body {
            background-color: #FFF8CC;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.set_option('deprecation.showPyplotGlobalUse', False)
    utl.inject_custom_css()
    utl.navbar_component()


if __name__ == "__main__":
    main()