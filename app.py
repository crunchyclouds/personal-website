import streamlit as st
from PIL import Image
from pathlib import Path

pg = st.navigation([st.Page("aboutme.py"), st.Page("cv.py"), st.Page("myinterests.py")])
pg.run()