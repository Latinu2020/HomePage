from pathlib import Path
import streamlit as st
from PIL import Image



current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
logo_pic= current_dir / "Code" / "Logo.png"
logo_pic_read=Image.open(logo_pic)


st.set_page_config(page_title="CODE", page_icon="📊")

html_page="""
<div style="width: 600px; padding: 50px;"</div>
<h1 style="border:3px solid Tomato; border-radius: 16px; text-align: center; text-shadow: 2px 2px 5px red; font-family: Arial;">  Code</h1>
"""
st.markdown(html_page.format(),unsafe_allow_html=True)
st.markdown("----")
st.image(logo_pic_read)
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

st.markdown("![Alt Text](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)")


