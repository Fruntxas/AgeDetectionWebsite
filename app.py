import streamlit as st
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np
from PIL import Image

BASE_URI = 'https://http://0.0.0.0:8000/images'

#Functions


#Page Layout
st.set_page_config(layout="wide")
'''# Age Detection'''

st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    data = uploaded_file.read()
    image = Image.open(data)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))

