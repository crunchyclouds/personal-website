
import streamlit as st
from PIL import Image
from pathlib import Path

#configuration
st.set_page_config(page_title="My Interests - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

#relevant files
img_mole = Image.open(r"images/mole.jpg")
img_slipknot_concert = Image.open(r"images/slipknot_concert.jpg")
img_moon = Image.open(r"images/moon.jpg")
img_weil = Image.open(r"images/weil_conjectures.jpg")
img_corpus = Image.open(r"images/corpusdelicti.jpg")
img_coffee = Image.open(r"images/coffee.jpg")

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
st.title("My Interests")
st.write("")
st.write("")
with st.container():
    st.subheader("Current favorites")
    left_column, middle_column, right_column = st.columns([1,3.5,5])
    with left_column:
        st.image(img_weil)
    with middle_column:
        st.subheader("The Weil Conjectures")
    with right_column:
        st.write("The Weil Conjectures is a great book about philosophy and mathematics."
                 " It's a biography-ish about Simone and Andre Weil's lives.")
    left_column, middle_column, right_column = st.columns([1, 3.5, 5])
    with left_column:
        st.image(img_corpus)
    with middle_column:
        st.subheader("Corpus Delicti")
    with right_column:
        st.write("Corpus Delicti is a French goth-rock band from the 90s. My favorite song is "
                 "'Absent Friend'.")
    left_column, middle_column, right_column = st.columns([1, 3.5, 5])
    with left_column:
        st.image(img_coffee)
    with middle_column:
        st.subheader("Indonesian Sumatra")
    with right_column:
        st.write("I'm currently having a natural processed bean from What's the Buzz in College "
                 "Station. It's a chocolatey taste that pairs well with a V60 brew.")
        st.caption("")
    st.write("##")
with st.container():
    st.write("---")
    st.subheader("My Hobbies")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_mole)
    with text_column:
        st.subheader("Chemistry is radical!")
        st.write("I love our ability to inspect and change properties at the molecular scale "
                 "and enjoy engaging with the field at every chance!")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_slipknot_concert)
    with text_column:
        st.subheader("Music")
        st.write("Listening to music and attending concerts is a lot of fun. I listen to all kinds of "
                 "music and play the tabla, a type of hand drum from India.")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_moon)
    with text_column:
        st.subheader("Astronomy")
        st.write("I like to spend clear nights with my telescope and some good music. I took this"
                 " photo with my 5-inch Dobsonian and a steady hand.")

