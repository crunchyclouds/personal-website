import streamlit as st
from PIL import Image
from pathlib import Path

#pages
about_me = st.Page("aboutme.py", title="About Me", icon=":material/emoji_people:")
cv = st.Page("cv.py", title="Curriculum Vitae", icon=":material/clinical_notes:")
myinterests = st.Page("myinterests.py", title="My Interests", icon=":material/flutter_dash:")

pg = st.navigation([about_me, cv, myinterests])
pg.run()