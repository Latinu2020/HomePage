from pathlib import Path
import streamlit as st
from PIL import Image

###########Path Settings

current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
resume_file = current_dir / "assets"/ "CV.pdf"
profile_pic= current_dir / "assets" / "profile-pic.png"

####---General Settings---
PAGE_TITLE ="DIGITAL CV | FLORIN ROTARU"
PAGE_ICON=":wave:"
NAME="FLORIN ROTARU"
DESCRIPTION= """
BIM Specialist, assisting enterpries.
"""
EMAIL = "florin_rot@yahoo.com"
SOCIAL_MEDIA= {
    "YouTube": "https://www.youtube.com/@florinr8921",
    "LinkedIn": "https://www.linkedin.com/"
}
PROJECTS={
    "✔️ BIM Workflows":"https://latinu2020-homepage-1--home-csvkf3.streamlit.app/BIM"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

#--LOAD CSS, PDF & PROFIL PIC

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)

######--hero section

col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION) 
    st.download_button(
        label="  Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("✉",EMAIL)   