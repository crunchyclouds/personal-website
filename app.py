import streamlit as st
import requests
from PIL import Image

#loading images etc in
img_double_helix = Image.open(r"C:\Users\mihir\Programs\Documents\GitHub\personal-website\images\double helix.webp")


st.set_page_config(page_title="Mihir's Webpage", page_icon=":ogre", layout="wide")

#homepage header
st.subheader("Hey, I'm Mihir! :wave:")
st.title("I'm a materials scientist studying at Texas A&M University.")
st.write("I love sharing my passions and incorporating my interest for computational methods into my research.")
st.write("[Learn more about me](https://www.linkedin.com/in/mihir-kalvakaalva)")

#my experiences
with st.container():
    st.write("---")
    st.header("Experiences")
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_double_helix)
    with text_column:
        st.subheader("Materials Scientist Intern at Xerion Advanced Battery")
        st.write("This past summer, I interned at an R&D Battery company, where I worked on "
                 "exciting topics relating to Li-ion batteries.")