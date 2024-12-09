import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Curriculum Vitae - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

img_engineering_showcase = Image.open(r"images/engineering_showcase.jfif")
img_xerion_group_photo = Image.open(r"images/xerion_group_photo.jfif")
img_chemistry_open_house = Image.open(r"images/chemistry_open_house.jpg")
img_happy_bacteria = Image.open(r"images/happy_bacteria.jpg")

with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.title("Curriculum Vitae")
        st.text("")
    with right_column:
        with open("images/Mihir Kalvakaalva Curriculum Vitae.pdf", "rb") as pdf_file:
            cv_pdf = pdf_file.read()
        st.download_button(
            label="CV",
            data=cv_pdf,
            file_name="Mihir Kalvakaalva Curriculum Vitae.pdf",
            mime="application/octet-stream")

    st.subheader("Research Appointments")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_xerion_group_photo)
        st.caption("June 2024 to August 2024")
        st.text("")
    with text_column:
        st.subheader("Materials Scientist Intern at Xerion Advanced Battery")
        st.write("This past summer, I interned at an R&D Battery company, where I worked on "
                    "exciting topics relating to Li-ion batteries.")
        st.text("")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_engineering_showcase)
        st.caption("December 2023 to June 2024")
        st.text("")
    with text_column:
        st.subheader("Project Lead on Vapor Compression Desalination")
        st.write("In 2024, I worked on a vapor compression desalination project under the "
                    "advice of Dr. Mark Holtzapple. We made substantial progress on the technology"
                    "and won 2nd at the Texas A&M Student Research Week.")
        st.text("")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_happy_bacteria)
        st.caption("September 2023 to May 2024")
        st.text("")
    with text_column:
        st.subheader("Biofuels Research Assistant")
        st.write("In the 2023-2024 school year, I assisted work on biofuel synthesis in the Holtzapple"
                    " Group. We used a variety of feedstocks and bacteria to produce carboxylic acids. I"
                    "worked both small-scale R&D and a steady-state fermentation system.")
        st.text("")

    st.subheader("Teaching and Leadership Roles")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_chemistry_open_house)
        st.caption("July 2024 to Current")
        st.text("")
    with text_column:
        st.subheader("Science Chair of SASE Texas A&M Chapter")
        st.write("In my ongoing role as Science Chair in the Society of Asian Scientists and Engineers,"
                    "I get to fulfill my interest in spreading interest in science at events like the A&M"
                    "Chemistry Open House")
        st.text("")

    st.subheader("Education")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("")
        st.caption("August 2022 to May 2026")
        st.text("")
    with text_column:
        st.subheader("Texas A&M University")
        st.write("Bachelor's of Science in Materials Science and Engineering")
        st.write("Minor in Mathematics")

    st.subheader("Awards and Honors")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("")
        st.caption("May 2024 to Present")
        st.text("")
    with text_column:
        st.subheader("Texas Entreprenuership in Energy Fellowship")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("")
        st.caption("March 2024")
        st.text("")
    with text_column:
        st.subheader("Texas A&M Student Research Week: 2nd Place Poster Presentation")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("")
        st.caption("July 2022")
        st.text("")
    with text_column:
        st.subheader("The Congressional Award: Gold Medal")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.write("")
        st.caption("August 2022 to January 2024")
        st.text("")
    with text_column:
        st.subheader("Texas A&M Engineering Honors")

