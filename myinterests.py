
import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="My Interests - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")


with st.container():
    st.header("Current favorites")
    left_column, middle_column, right_column = st.columns([1,3.5,5])
    with left_column:
        st.caption("")
        st.link_button(label="Goodreads", url="https://www.goodreads.com/book/show/41940441-the-weil-conjectures")
        st.caption("")
        st.link_button(label="Spotify", url="https://open.spotify.com/artist/7gS5jg683LHmjEY540cmH5?si=244bd3e5601041e8")
        st.caption("")
    with middle_column:
        st.subheader("The Weil Conjectures")
        st.caption("Current favorite book")
        st.subheader("Corpus Delicti")
        st.caption("Current favorite band")
        st.subheader("Natural Indonesian Sumatra")
        st.caption("Current coffee bean")
    with right_column:
        st.write("The Weil Conjectures is a great book (so far) about philosophy and mathematics."
                 " It's a almost-biography about Simone and Andre Weil's lives.")
        st.caption("")
        st.write("Corpus Delicti is a French goth-rock band from the 90s. My favorite song is "
                 "'Absent Friend'.")
        st.caption("")
        st.write("I'm currently having a natural processed bean from What's the Buzz in College "
                 "Station. It's a chocolatey taste that pairs well with a V60 brew.")
        st.caption("")



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
        st.write("Listening to music and attending concerts is a lot of fun.")
