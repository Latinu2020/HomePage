import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈")


html_page="""
<head>
<meta charset="utf-8">
<title>Effect of CSS Padding on Element Box Size</title>
<style>
    div {
        width: 100%;
        padding: 25px;
        background: violet;
    }
</style>
</head>
<body>
    <div>
        <h1>This is a DIV Box</h1>
    </div>
    <p><strong>Notice</strong>, the scrollbar at the bottom of the viewport.</p>
</body>
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

"""### My Project"""
st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")