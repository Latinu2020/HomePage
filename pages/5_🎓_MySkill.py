from pathlib import Path
import streamlit as st
from PIL import Image


###########Path Settings

current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
udemy_pic= current_dir / "skill" / "udemy.jpg"
udemy_pic_read=Image.open(udemy_pic)
autodesk_pic= current_dir / "skill" / "autodesk.jpg"
autodesk_pic_read=Image.open(autodesk_pic)
st.set_page_config(page_title="Skill", page_icon="📊",layout="wide")
st.markdown("----")
st.title("# Skill")
st.markdown("----")

col1,col2=st.columns(2,gap="large")
with col1:
    container1=st.container()
    container1.subheader("UDEMY")
    container1.image(udemy_pic_read, width=400)
    container1.markdown("""<span style="word-wrap:break-word;">Udemy is a platform that allows instructors to build online courses on their preferred topics. 
        -Using Udemy's course development tools, instructors can upload videos, source code for developers,
        PowerPoint presentations, PDFs, audio, ZIP files and any other content that learners might find helpful.
        -Instructors can also engage and interact with users via online discussion boards.</span>""",unsafe_allow_html=True)
with col2:
    container2=st.container()
    container2.subheader("AUTODESK UNIVERSITY")
    container2.image(autodesk_pic_read, width=350)
    container2.text("""
        -Autodesk, Inc. is an American multinational software corporation that makes software products and services
        for the architecture, engineering, construction, manufacturing, media, education, and entertainment industries.
        -Autodesk offers certificates in two categories: Autodesk Certified User and Advanced Certified Professional.
        -Autodesk Certified User- Verifies entry-level skills in key Autodesk products. 
        Designed for students and instructors who wish to demonstrate basic proficiency. 
        Curriculum, courseware, and exams offered for independent study or institutional integration.
        -Advanced Certified Professional- Validates more advanced skills, including complex workflow and design challenges. 
        Designed for students seeking a competitive advantage in a specific product area.
    """)
st.header("My Certification")
st.markdown("----")   