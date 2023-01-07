import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈")


html_page="""
<div style="width: 600px; padding: 50px;"</div>
<h1 style="border:3px solid Tomato; border-radius: 10px; text-align: center; font-family: Arial; background-color: #96ceb4;">Hello World</h1>
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

"""### My Project"""
st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")