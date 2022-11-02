import streamlit as st

import utils as utl

import random

import os

img_list = []

@utl.find_picture
def list(src):
    img_list.append(src)


def load_view():
    list()
    st.title('Home Page')
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        scriptpath = os.path.dirname(__file__)
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        with open(os.path.join(scriptpath + "/../data",image_file.name),"wb") as f: 
            f.write(image_file.getbuffer())         
            st.success("Saved File")
    st.image(random.choice(img_list))
    