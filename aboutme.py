import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="About me - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

#homepage header
st.subheader("About me")
st.title("I'm a materials scientist studying at Texas A&M University.")
st.write("[Contact me via LinkedIn](https://www.linkedin.com/in/mihir-kalvakaalva)")


with st.container():
    st.write("---")
    st.header("Mihir Kalvakaalva")
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_xerion_group_photo)
    with text_column:
        st.subheader("Undergraduate Student at Texas A&M University")
        st.write("This past summer, I interned at an R&D Battery company, where I worked on "
                    "exciting topics relating to Li-ion batteries.")