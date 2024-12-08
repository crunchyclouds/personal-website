import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Curriculum Vitae - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

img_engineering_showcase = Image.open(r"images/engineering_showcase.jfif")
img_xerion_group_photo = Image.open(r"images/xerion_group_photo.jfif")
img_chemistry_open_house = Image.open(r"images/chemistry_open_house.jpg")
img_happy_bacteria = Image.open(r"images/happy_bacteria.jpg")

with st.container():
    st.write("---")
    st.header("My Experiences")
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

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_happy_bacteria)
    with text_column:
        st.subheader("Biofuels Research Assistant")
        st.write("In the 2023-2024 school year, I assisted work on biofuel synthesis in the Holtzapple"
                    " Group. We used a variety of feedstocks and bacteria to produce carboxylic acids. I"
                    "worked both small-scale R&D and a steady-state fermentation system.")

