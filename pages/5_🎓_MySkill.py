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

st.markdown("<h1 style='text-align: center; color: red; font-size: 70px; text-decoration-line:'>Skill</h1>",unsafe_allow_html=True)
st.markdown("----")

col1,col2=st.columns(2,gap="large")
with col1:  
    st.subheader("UDEMY")
    st.image(udemy_pic_read, width=350)
    st.markdown("""<span style="word-wrap:break-word;">Udemy is a platform that allows instructors to build online courses on their preferred topics. 
        Using Udemy's course development tools, instructors can upload videos, source code for developers,
        PowerPoint presentations, PDFs, audio, ZIP files and any other content that learners might find helpful.
        Instructors can also engage and interact with users via online discussion boards.</span>""",unsafe_allow_html=True)
with col2:
   
    st.subheader("AUTODESK UNIVERSITY")
    st.image(autodesk_pic_read, width=350)
    st.markdown("""<span style="word-wrap:break-word;">Autodesk, Inc. is an American multinational software corporation that makes software products and services
        for the architecture, engineering, construction, manufacturing, media, education, and entertainment industries.Autodesk offers certificates in two categories: Autodesk Certified User and Advanced Certified Professional.
        Autodesk Certified User- Verifies entry-level skills in key Autodesk products. 
        Designed for students and instructors who wish to demonstrate basic proficiency. 
        Curriculum, courseware, and exams offered for independent study or institutional integration.
        Advanced Certified Professional- Validates more advanced skills, including complex workflow and design challenges. 
        Designed for students seeking a competitive advantage in a specific product area.</span>""",unsafe_allow_html=True)
st.header("My Certification")
st.markdown("----")

####prepared certificate Udemy  
c1_pic= current_dir / "skill" / "1.jpg"
c1_pic_read=Image.open(c1_pic)
c2_pic= current_dir / "skill" / "2.jpg"
c2_pic_read=Image.open(c2_pic)
c3_pic= current_dir / "skill" / "3.jpg"
c3_pic_read=Image.open(c3_pic)
c4_pic= current_dir / "skill" / "4.jpg"
c4_pic_read=Image.open(c4_pic)
c5_pic= current_dir / "skill" / "5.jpg"
c5_pic_read=Image.open(c5_pic)
c6_pic= current_dir / "skill" / "6.jpg"
c6_pic_read=Image.open(c6_pic)
c7_pic= current_dir / "skill" / "7.jpg"
c7_pic_read=Image.open(c7_pic)
c8_pic= current_dir / "skill" / "8.jpg"
c8_pic_read=Image.open(c8_pic)
c9_pic= current_dir / "skill" / "9.jpg"
c9_pic_read=Image.open(c9_pic)
c10_pic= current_dir / "skill" / "10.jpg"
c10_pic_read=Image.open(c10_pic)
c11_pic= current_dir / "skill" / "11.jpg"
c11_pic_read=Image.open(c11_pic)

col3,col4=st.columns(2,gap="large")
with col3:
    expander = st.expander("👉 SEE UDEMY CERTIFICATION")
    expander.write("""
    BELOW YOU CAN FIND MY CERTIFICATES OBTAINED
    THROUGH COURSES PURCHASED FROM UDEMY
    """)
    expander.image(c1_pic_read,width=550)
    expander.image(c2_pic_read,width=550)
    expander.image(c3_pic_read,width=550)
    expander.image(c4_pic_read,width=550)
    expander.image(c5_pic_read,width=550)
    expander.image(c6_pic_read,width=550)
    expander.image(c7_pic_read,width=550)
    expander.image(c8_pic_read,width=550)
    expander.image(c9_pic_read,width=550)
    expander.image(c10_pic_read,width=550)
    expander.image(c11_pic_read,width=550)
with col4:
    expander = st.expander("See Autodesk Certification 👈")
    expander.write("""
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
    """)
    expander.image("https://static.streamlit.io/examples/dice.jpg") 
           