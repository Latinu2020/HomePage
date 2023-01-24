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
-BIM/Digital Engineering specialist and professionally qualified Mechanical Engineer with immense 6+year
experience in Revit, Plant3D, Advance Steel and Mechanical modeling, Scan to BIM, Coordination and
Design optimization
-Multiple Projects Co-ordination including High-Rise, Commercial Buildings and Process Plant Layout and
Piping Design.
-I have achieved high productivity and time efficiency in BIM projects simultaneously using Revit, Autocad
Plant3D and Navisworks for clash detection.
-Being a BIM practitioner and having a solid background in BIM/VDC with sound knowledge in Revit,
Autocad Plant3D and Navisworks
-I have had opportunities to render my services to take the project from a nascent stage to develop fully
from design to construction set of documentation through various necessary stages with complete Co-ordination
and management
"""
EMAIL = "florin_rot@yahoo.com"
SOCIAL_MEDIA= {
    "🎬YouTube": "https://www.youtube.com/@florinr8921",
    "👔LinkedIn": "https://www.linkedin.com/"
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
<div style="width: 1050px;"</div>
<h1 style="text-align: center; text-indent: 70px; color: white; font-size: 80px; text-shadow: 10px 10px 20px #000000; font-family: "Fantasy">Welcome</h1>
"""
st.markdown(html_page.format(),unsafe_allow_html=True)
st.markdown("----")
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=200)
with col2:
    st.title(NAME)
    st.text(DESCRIPTION) 
    st.download_button(
        label="📂 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("✉",EMAIL) 
    st.markdown("----")

####--SOCIAL LINKS--
st.write("#")
cols= st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#---Experience & Qualifications--
st.write("#")
st.subheader("✒Experience & Qualifications")
st.markdown("----")
st.write(
     """
    -✓ ###########################
    -✓###########222222
    -✓##############################333
    """
)
#---SKILLS--
st.write("#")
st.subheader("🏆Hard Skills")
st.markdown("----")
st.write(
     """
    - 🏅Team player/leader capable of manage multidiscipline modellers and drafters. Recently working as project BIM manager on multidiscipline projects and managing modellers from around Australia and overseas
    - 🏅Define workflow, create standard, implementation standards, manage the resources, estimate time. Capable to provide training locally or remotely for implementation of standards. Great communication skills
    - 🏅Passionate about BIM implementation not only in modelling but also in assess management, cost estimate and its impact on design procedure
    - 🏅AutoCAD Plant 3D, Revit and Civil 3D customisation, utilizing programming to reduce manual works and increase productivity, use Python to create parametric catalogue items
    - 🏅Knowing how to use and understanding the pros and cons of many software including Plant 3D, Civil 3D, Revit, Inventor, Solidworks, Infraworks and Navisworks. Able to create templates, parametric catalogue items, families for design software
    """
)


##############--work history
#st.write("#")
#st.subheader("Work History")
#st.write("---")

###--job#
#### Reduce header
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:3rem;}
        div.block-container {padding-bottom:3rem;}
        div.block-container {padding-left:3rem;}
        div.block-container {padding-right:3rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)