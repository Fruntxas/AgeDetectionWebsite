import streamlit as st
from streamlit_webrtc import webrtc_streamer, ClientSettings
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
import cv2
from autocrop import Cropper

#BASE_URL = 'https://agedetection-tyxhjmug3a-ew.a.run.app/image'  #Tiago
BASE_URL = 'https://agedetection-m2ianlcoya-ew.a.run.app/image'   #Felix

#Page Layout

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Age Detection</h1>", unsafe_allow_html=True)

col1, col2 = st.beta_columns((1,1))
files=None

with col1:

    st.markdown("<h1 style='text-align: center;'>1) Upload an Image!</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type="jpg")


    if uploaded_file is not None:
        with open("tmp.png", "wb+") as data:
            data.write(uploaded_file.read())

        #st.markdown("<h2 style='text-align: center;'>This is your uploaded Image:</h1>", unsafe_allow_html=True)
        '''## This is your uploaded Image:'''
        image_normal = Image.open(uploaded_file)
        st.image(image_normal, caption='', width=300)
        cropper = Cropper(width=300, height=300)
        cropped_array = cropper.crop("tmp.png")
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save('cropped.png')
        image_cropped = Image.open('cropped.png')


        files = {'file':uploaded_file.getvalue()
                }
#if files != None:

    with col2:
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(240, 242, 246);
            height: 10em;
            width: 30em;


        }
        </style>""", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>2) Push the Button!</h1>", unsafe_allow_html=True)
        if st.button('Predict the Age'):
            '''## First we crop and resize your image'''
            st.image(image_cropped, caption='', use_column_width=False)

            response = requests.post(
                BASE_URL,
                files=files
            )

            st.write("Your age is between: ")
            st.write(response.json()['Initial Age Bin'])
            st.write('And we think you look like:')
            st.write(int(response.json()['Weighted Guess']))
            st.balloons()
