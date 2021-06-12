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
from autocrop import Cropper

#BASE_URL = 'https://agedetection-tyxhjmug3a-ew.a.run.app/image'  #Tiago
BASE_URL = 'https://agedetection-m2ianlcoya-ew.a.run.app/image'   #Felix


#Page Layout

st.set_page_config(layout="wide")
'''# Age Detection!'''
col1, col2, col3, col4= st.beta_columns((4, 1,1,1))

st.sidebar.markdown(f"""
    # Choose your Option:
    """)

option = st.sidebar.selectbox('', ['Upload an Image', 'Webcam Feed'])

if option == 'Upload an Image':
    with col1:
        st.title("Upload an Image")
        uploaded_file = st.file_uploader("", type="jpg")


        if uploaded_file is not None:
            with open("tmp.png", "wb+") as data:
                data.write(uploaded_file.read())

            st.write('Uploaded Image')
            image_normal = Image.open(uploaded_file)
            st.image(image_normal, caption='', width=300)

            st.write('Cropped Image')
            cropper = Cropper(width=100, height=100)
            # Get a Numpy array of the cropped image
            cropped_array = cropper.crop("tmp.png")
            # Save the cropped image with PIL
            cropped_image = Image.fromarray(cropped_array)
            cropped_image.save('cropped.png')
            image_cropped = Image.open('cropped.png')
            st.image(image_cropped, caption='', use_column_width=False)


            files = {'file':uploaded_file.getvalue()
                    }


else:
    with col1:
        st.title("Webcam Live Feed")
        webrtc_streamer(
            client_settings=ClientSettings(
                rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                media_stream_constraints={"video": True, "audio": False},
            ),
            key="WebcamFeed",
        )


with col3:
    if st.button('Predict the Age!'):

        response = requests.post(
            BASE_URL,
            files=files
        )
        st.write("Thinking...")
        st.write(response.json()['Guess'])
        st.balloons()



# run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     st.write('Stopped')


