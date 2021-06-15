import streamlit as st
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
from autocrop import Cropper

#BASE_URL = 'https://agedetection-tyxhjmug3a-ew.a.run.app/image'  #Tiago
BASE_URL = 'https://agedetection-m2ianlcoya-ew.a.run.app/image'   #Felix

#Page Layout

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; font-size: 50;'>Age Detection</h1>", unsafe_allow_html=True)

col1, col2,col3,col4,col5,col6 = st.beta_columns((1,4,1,1,4,1))
files=None

with col2:

    st.markdown("<h1 style='text-align: center;'>1) Upload an Image!</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type="jpg")


    if uploaded_file is not None:
        with open("tmp.png", "wb+") as data:
            data.write(uploaded_file.read())
        '''### This is your uploaded Image:'''
        image_normal = Image.open(uploaded_file)
        st.image(image_normal, caption='', width=300)
        cropper = Cropper(width=200, height=200)
        cropped_array = cropper.crop("tmp.png")
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save('cropped.png')
        image_cropped = Image.open('cropped.png')


        files = {'file':uploaded_file.getvalue()
                }


if files != None:
    with col5:
        st.markdown("<h1 style='text-align: center;'>2) Push the Button!</h1>", unsafe_allow_html=True)

        m = st.markdown("""
        <style>
        div.stButton > button:first-child {

            width: 100%;
            height: 80px;
            flex-direction: column;}

        </style>""", unsafe_allow_html=True)

        if st.button('Predict the Age'):
            '''### First we crop and resize your image'''
            st.image(image_cropped, caption='', use_column_width=False)

            response = requests.post(
                BASE_URL,
                files=files
            )
            age_bin=response.json()['Initial Age Bin']
            guess = int(response.json()['Weighted Guess'])

            st.markdown(f'# Your age is between: **{age_bin}**')
            st.markdown(f'# And we think you look like: **{guess}**')
            st.balloons()
