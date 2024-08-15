import streamlit as st
import glob
from streamlit_image_select import image_select

def load_images():
    image_files = glob.glob("imgs/*/*.jpg")
    manuscripts = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()

    return image_files, manuscripts

image_files, manuscripts = load_images()
view_manuscripts = st.multiselect("Select Folder(s)", manuscripts)
st.markdown('#')

def img_option(image_files, view_manuscripts):
    view_images = []
    for image_file in image_files:
        if any(manuscript in image_file for manuscript in view_manuscripts):
            view_images.append(image_file)

    im =image_select(label="select", images=view_images, use_container_width=False, index=-1)
        # st.write(im)
    return im
