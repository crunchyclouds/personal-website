
import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Curriculum Vitae - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

img_mole = Image.open(r"images/mole.jpg")
img_slipknot_concert = Image.open(r"images/slipknot_concert.jpg")

with st.container():
    st.write("---")
    st.header("My Interests")
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_mole)
    with text_column:
        st.subheader("Chemistry is Radical!")
        st.write("I love the ability to inspect atomic and molecular properties and seeing how"
                    " those changes propagate to the macroscale. Here's me with a mole :)")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_slipknot_concert)
    with text_column:
        st.subheader("Music")
        st.write("Listening to music and attending concerts is a lot of fun. My current favorite "
                    "artist is Siouxsie and the Banshees.")
