import streamlit as st
from PIL import Image
from pathlib import Path

#loading images etc in
img_engineering_showcase = Image.open("images/engineering_showcase.jfif")
img_xerion_group_photo = Image.open("images/xerion_group_photo.jfif")
img_chemistry_open_house = Image.open("images/chemistry_open_house.jpg")

st.set_page_config(page_title="Mihir's Webpage", page_icon=":ogre", layout="wide")

#homepage header
st.subheader("Hey, I'm Mihir! :wave:")
st.title("I'm a materials scientist studying at Texas A&M University.")
st.write("I love learning about chemistry and sharing my love for science with others!")
st.write("[Contact me via LinkedIn](https://www.linkedin.com/in/mihir-kalvakaalva)")

#my experiences

with st.container():
    st.write("---")
    st.header("Experiences")
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_xerion_group_photo)
    with text_column:
        st.subheader("Materials Scientist Intern at Xerion Advanced Battery")
        st.write("This past summer, I interned at an R&D Battery company, where I worked on "
                 "exciting topics relating to Li-ion batteries.")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_engineering_showcase)
    with text_column:
        st.subheader("Project Lead on Vapor Compression Desalination")
        st.write("In 2024, I worked on a vapor compression desalination project under the "
                 "advice of Dr. Mark Holtzapple. We made substantial progress on the technology"
                 "and won 2nd at the Texas A&M Student Research Week.")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_chemistry_open_house)
    with text_column:
        st.subheader("Science Chair of SASE Texas A&M Chapter")
        st.write("In my ongoing role as Science Chair in the Society of Asian Scientists and Engineers,"
                 "I get to fulfill my interest in spreading interest in science at events like the A&M"
                 "Chemistry Open House")
