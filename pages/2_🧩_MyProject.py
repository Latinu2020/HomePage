import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈")


html_page="""
<div {
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;
<h1 style="border:2px solid Tomato; text-align: center; font-family: Arial;">Hello World</h1>
</div>
}
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

"""### My Project"""
st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")