from pathlib import Path
import streamlit as st
from PIL import Image


###########Path Settings

current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
udemy_pic= current_dir / "skill" / "udemy.jpg"
udemy_pic_read=Image.open(udemy_pic)
autodesk_pic= current_dir / "skill" / "autodesk.png"
autodesk_pic_read=Image.open(autodesk_pic)
st.set_page_config(page_title="Skill", page_icon="📊")

st.title("# Skill")
st.markdown("####.")

col1,col2=st.columns(2)
with col1:
    st.subheader("UDEMY")
    st.image(udemy_pic_read, width=300)
with col2:
    st.subheader("AUTODESK")
    st.image(autodesk_pic_read, width=300)
   