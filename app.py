import streamlit as st
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np
from PIL import Image
import tempfile
import cv2

#BASE_URL = 'https://agedetection-tyxhjmug3a-ew.a.run.app/image'  #Tiago
BASE_URL = 'https://agedetection-m2ianlcoya-ew.a.run.app/image'   #Felix



#Page Layout

st.set_page_config(layout="wide")
'''# Age Detection'''
col1, col2,col3,col4= st.beta_columns((3, 1,1,1))

with col1:
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', width=300)

        files = {'file':uploaded_file.getvalue()
                }

        response = requests.post(
            BASE_URL,
            files=files
        )

with col3:
    if st.button('Predict the Age!'):
        st.write("Thinking...")
        st.write(response.json()['Guess'])
        st.balloons()


st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')


