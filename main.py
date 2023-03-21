import time
import streamlit as st
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.set_page_config(
    page_title="OCR",
    page_icon="🧊",
)
st.title("Optical Character Recognition")
st.write("Transform images into editable text with ease!!")


def extract_text(image):
    with st.spinner('Extracting text...'):
        output_text = pytesseract.image_to_string(image)
        time.sleep(1)
    st.success('Done!')
    st.write("Extracted Text:")
    st.write(output_text)


upload_image = st.sidebar.file_uploader(
    'Upload an image', type=["jpg", "png", "jpeg"])
if upload_image is not None:
    img = Image.open(upload_image)
    st.image(upload_image)
    if st.button("Extract Text"):
        extract_text(img)
