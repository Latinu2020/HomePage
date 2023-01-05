from pathlib import Path
import streamlit as st
from PIL import Image


###########Path Settings

current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
linux_pic= current_dir / "distro" / "Linux.png"
unix1_pic= current_dir / "distro" / "freebsd.png"
unix2_pic= current_dir / "distro" / "openbsd.png"
unix3_pic= current_dir / "distro" / "netbsd.png"
windows_pic= current_dir / "distro" / "windows.png"
st.set_page_config(page_title="Distro", page_icon="📊")

st.title("# Distro")
st.markdown("A set of software components, often open source, that have been packaged into a larger product or component for distribution to end-users.")

col1,col2,col3,col4,col5=st.columns(5,gap="small")
with col1:
    st.image(linux_pic, width=230)
with col2:
    st.image(unix1_pic, width=230)
with col3:
    st.image(unix2_pic, width=230)
with col4:
    st.image(unix3_pic, width=230)
with col5:
    st.image(windows_pic, width=230)    