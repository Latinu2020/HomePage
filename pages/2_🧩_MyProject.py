import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈",layout="wide")


html_page="""
@keyframes example {
  from {background-color: red;}
  to {background-color: yellow;}
}
<div style="width: 600px; padding: 50px; animation-name: example; animation-duration: 7s;"</div>
<h1 style="border:3px solid Tomato; border-radius: 12px; text-align: center; text-shadow: 2px 2px 5px red; font-family: Arial;">  My Project</h1>
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")