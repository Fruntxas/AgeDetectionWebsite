import streamlit as st
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras import models
import tempfile

BASE_URL = 'https://agedetection-tyxhjmug3a-ew.a.run.app/image'

#Functions


#Page Layout
st.set_page_config(layout="wide")
'''# Age Detection'''

st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    files = {'file':uploaded_file.getvalue()
            }

    response = requests.post(
        BASE_URL,
        files=files
    )

    # st.write("")
    st.write("Classifying...")
    st.write(response.json()['Guess'])
    st.balloons()









