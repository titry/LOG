import streamlit as st

import utils as utl

@utl.find_picture
def show(src):
    st.image(src)

def load_view():
    st.title('Daily Page')

    show()