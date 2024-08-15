import streamlit as st
from predictor import predict
from PIL import Image
from streamlit_image_select import image_select
from io import BytesIO
import glob
from vidPredictor import vid

st.set_page_config(page_title="Accident Detecton", page_icon= ":collision:", layout="centered")
st.title(" Accident Detection using machine learning")
st.divider()



def load_options():
    options =[]
    addresses =glob.glob('options/*')
    for file in addresses:
        file = file.replace("\\", "/")
        parts = file.split('/')
        if parts[-1] not in options:
            options.append(parts[-1])
    option = dict(zip(options, addresses))
    return option

def vid_op(f):
    label, image =vid(f)
 
    col1, col2 = st.columns(2)
    col2.markdown("###")
    with col1:
        im =image_select(label="", captions=label , images=image, use_container_width=True, index=0, return_value="index")
    with col2:
        with st.container(border=True):
            st.write(label[im])
            st.image(image[im])

def img_op(f):
    st.write(predict(Image.open(f).resize((250,250))))
    st.image(f)



uploaded_file = st.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg', 'mp4'])
try:
    if uploaded_file.type[-3:] == 'mp4':
        vid_op(uploaded_file)  #video function call
    else:
        img_op(uploaded_file)
except:
    st.warning("Please upload a file")


st.markdown('#')
st.subheader("OR Choose from below")
st.markdown('#')


option = load_options()
view_options = st.selectbox("Select your option", option.keys(),index=None)
try:
    if view_options[-3:] == 'mp4':
        st.video(option[view_options])
        with open(option[view_options], '+rb') as fh:
            buf = BytesIO(fh.read())
        vid_op(buf)
    else:
        a = glob.glob(option[view_options]+'/*')
        col1, col2 = st.columns(2)
        col2.markdown("###")
        with col1:
            im =image_select(label="select", images=a, use_container_width=False, index=-1)
        with col2:
            img_op(im)
except:
    st.warning("Please choose a file")
