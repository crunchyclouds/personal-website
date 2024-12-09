import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="About me - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

img_rev_photo = Image.open(r"images/rev_photo.jpg")

with st.container():
    left_column, text_column = st.columns((1,2))
    with left_column:
        st.image(img_rev_photo)
        st.header("Mihir Kalvakaalva")
        st.write("Student researcher at Banerjee Research Laboratory")
        st.link_button(label="Email", url="mihir.38k@gmail.com", icon=":material/mail:")
        st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/mihir-kalvakaalva/", icon=":material/linked_services:")
    with text_column:
        st.title("About me")
        st.write("Howdy, I'm studying materials science and engineering at Texas A&M."
                 "My ongoing research focuses on the synthesis of phase transition "
                 "oxides for batteries. I love learning about topics of physical and "
                 "inorganic chemistry.")
        st.write("")
        st.write("On campus, I'm also a tutor for our materials science department "
                 "and the science chair of my student organization, The Society of "
                 "Asian Scientists and Engineers.")
        st.write("")
        st.write("At home, I love engaging with my hobbies. Pour-over coffee and amateur "
                 "astronomy are a couple of my big ones. There's so much fun science and "
                 "beauty to be observed in them!")
