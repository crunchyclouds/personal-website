import streamlit as st
from PIL import Image
from pathlib import Path

#config
st.set_page_config(page_title="About me - Mihir Kalvakaalva", page_icon=":ogre", layout="wide")

#relevant files
img_rev_photo = Image.open(r"images/rev_photo.jpg")

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
    st.title("About me")
    st.write("###")
    left_column, right_column = st.columns((1,2))
    with left_column:
        st.image(img_rev_photo, width=450)
        st.header("Mihir Kalvakaalva")
        st.write("Student researcher at Banerjee Research Laboratory")
    with right_column:
        st.write("Howdy, I'm studying materials science and engineering at Texas A&M University. "
                 "My ongoing research in the Banerjee Group focuses on the synthesis of phase transition "
                 "oxides for batteries. I love learning about topics of physical and "
                 "inorganic chemistry.")
        st.write("")
        st.write("On campus, I'm a tutor for our materials science department "
                 "and the science chair of my student organization, The Society of "
                 "Asian Scientists and Engineers.")
        st.write("")
        st.write("At home, I love engaging with my hobbies. Pour-over coffee and amateur "
                 "astronomy are a couple of my big ones. There's so much fun science and "
                 "beauty to be observed in the natural world!")

    left_column, right_column = st.columns((1, 7))
    with left_column:
        if st.button(label="Email", icon=":material/mail:"):
            with right_column:
                st.write(r"mihir.38k@gmail.com")
        st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/mihir-kalvakaalva/",
                       icon=":material/linked_services:")