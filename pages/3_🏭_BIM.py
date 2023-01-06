from pathlib import Path
import streamlit as st
from PIL import Image


###########Path Settings

current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
B_pic= current_dir / "BIM" / "BIM01.png"
B_pic_read=Image.open(B_pic)
C_pic= current_dir / "BIM" / "BIM02.png"
C_pic_read=Image.open(C_pic)

st.set_page_config(page_title="BIM", page_icon="🌍",layout="wide")

st.markdown("<h1 style='text-align: center; color: MediumAquamarine; font-size: 70px; text-decoration-line:'>BIM</h1>",unsafe_allow_html=True)
st.markdown(
    """Building information modeling (BIM) is a process supported by various tools, technologies and contracts
    involving the generation and management of digital representations of physical and functional characteristics of places. 
    Building information models (BIMs) are computer files (often but not always in proprietary formats and containing
    proprietary data) which can be extracted, exchanged or networked to support decision-making regarding a built asset. 
    BIM software is used by individuals, businesses and government agencies who plan, design, construct, operate and maintain
    buildings and diverse physical infrastructures, such as water, refuse, electricity, gas, communication utilities, roads, 
    railways, bridges, ports and tunnels.
    """
)

col1,col2=st.columns(2,gap="large")

with col1:
    st.markdown("<h1 style='text-align: center; color: #BFDAF7; font-size: 20px; text-decoration-line:'>Level of Project</h1>",unsafe_allow_html=True)
    st.image(B_pic_read)
with col2:
    st.markdown("<h1 style='text-align: center; color: #BFDAF7; font-size: 20px; text-decoration-line:'>BIM Levels</h1>",unsafe_allow_html=True)
    st.image(C_pic_read)    