import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈")


html_page="""
<h1 style="border:2px solid Tomato;">Hello World</h1>
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

"""### My Project"""
st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")