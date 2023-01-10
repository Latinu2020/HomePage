from pathlib import Path
import streamlit as st
from PIL import Image



current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
logo_pic= current_dir / "Code" / "Logo.png"
logo_pic_read=Image.open(logo_pic)


st.set_page_config(page_title="CODE", page_icon="📊",layout="wide")
html_page="""
<div style="width: 1050px; padding: 0px;"</div>
<h1 style="text-align: left; text-indent: 70px; color: white; font-size: 80px; text-shadow: 10px 10px 20px #000000; font-family: "Fantasy">Code</h1>
"""

col1, col2, col3 = st.columns(3)
with col1:
    st.text("""
_♥__♥_____♥__♥___ Put This
_♥_____♥_♥_____♥__ Heart
_♥______♥______♥__ On Your
__♥_____/______♥__ Page If
___♥____\_____♥___ You Had
____♥___/___♥_____ Your Heart
______♥_\_♥_______ Broken
________♥_________…………….

 
""")
with col2:
    st.markdown(html_page.format(),unsafe_allow_html=True)
with col3:
    st.image(logo_pic_read)

st.markdown("----")

st.markdown("![Alt Text](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)")


