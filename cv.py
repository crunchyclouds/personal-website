import streamlit as st
from PIL import Image
from pathlib import Path

#config
st.set_page_config(page_title="Curriculum Vitae - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

#relevant files
img_engineering_showcase = Image.open(r"images/engineering_showcase.jfif")
img_xerion_group_photo = Image.open(r"images/xerion_group_photo.jfif")
img_chemistry_open_house = Image.open(r"images/chemistry_open_house.jpg")
img_happy_bacteria = Image.open(r"images/happy_bacteria.jpg")
img_rev_photo = Image.open(r"images/rev_photo.jpg")
img_zachry = Image.open(r"images/zachry.jpg")

#navigation menu
with st.container():
    t0, t1, t2, t3 = st.columns((1,1,1,1))
    with t0:
        st.page_link("aboutme.py", label="Mihir Kalvakaalva",)
    with t1:
        st.page_link("aboutme.py", label="About Me", icon=":material/emoji_people:")
    with t2:
        st.page_link("cv.py", label="Curriculum Vitae", icon=":material/clinical_notes:")
    with t3:
        st.page_link("myinterests.py", label="My Interests", icon=":material/flutter_dash:")
st.write("---")
st.write("###")


#body
with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.title("Curriculum Vitae")
    with right_column:
        st.text("")
        st.text("")
        with open("images/Mihir Kalvakaalva Curriculum Vitae.pdf", "rb") as pdf_file:
            cv_pdf = pdf_file.read()
        st.download_button(
            label="Curriculum Vitae (a more detailed version)",
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
                    " Group. We used a variety of feedstocks and bacteria to produce carboxylic acids. I "
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
        st.write("In my ongoing role as Science Chair in the Society of Asian Scientists and Engineers, "
                    "I get to fulfill my interest in spreading interest in science at events like the TAMU "
                    "Chemistry Open House.")
        st.text("")

    st.subheader("Education")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_zachry)
        st.caption("August 2022 to May 2026")
        st.text("")
    with text_column:
        st.subheader("Texas A&M University")
        st.write("I'm pursuing a Bachelor's of Science in Materials Science and "
                 "Engineering at Texas A&M University. I'm also completing a minor "
                 "in Mathematics. I will be graduating in Spring 2026 with intention to "
                 "pursue further studies in chemistry and materials science.")
