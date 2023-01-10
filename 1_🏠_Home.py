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
Mr. Rotaru has a BSc Degree in Mechanical Engineering, with a Diploma for Oil Field Equipment. He
has over 10 years of experience at mechanical engineering, detailed designer and CAD. These skills
have been effectively used on many projects while executing. He uses his knowledge and experience
to ensure that each project is performed on time, within budget, and completed in a high-quality
manner to the satisfaction of the company for the feasibility studies, proposals and projects executed
in the office.
He currently manages software for each project in BIM/CAD department for performed on time and
give supports for the teams in the project
"""
EMAIL = "florin_rot@yahoo.com"
SOCIAL_MEDIA= {
    "YouTube": "https://www.youtube.com/@florinr8921",
    "LinkedIn": "https://www.linkedin.com/"
}
PROJECTS={
    "✔️ BIM Workflows":"https://latinu2020-homepage-1--home-csvkf3.streamlit.app/BIM"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

#--LOAD CSS, PDF & PROFIL PIC

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)

######--hero section
html_page="""
<div style="width: 1050px; padding: 70px;"</div>
<h1 style="border:3px solid Tomato; border-radius: 16px; text-align: center; color: white; text-shadow: 2px 2px 4px #000000; font-family: Arial;">👍Welcome</h1>
"""
st.markdown(html_page.format(),unsafe_allow_html=True)
st.markdown("----")
col1,col2=st.columns(2)
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION) 
    st.download_button(
        label="📂 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📨",EMAIL) 

####--SOCIAL LINKS--
st.write("#")
cols= st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#---Experience & Qualifications--
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
     """
    - ###############11111111111111111111111111
    - ###########222222
    - ##############################333
    """
)
#---SKILLS--
st.write("#")
st.subheader("Hard Skills")
st.write(
     """
    - ✅###############11111111111111111111111111
    - ✅###########222222222222222222222222222222
    - ✅##############################33333333333
    """
)


##############--work history
st.write("#")
st.subheader("Work History")
st.write("---")

###--job#
