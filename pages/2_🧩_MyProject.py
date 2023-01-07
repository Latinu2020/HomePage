import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈",layout="wide")


def navigation_bar():
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["Home", "Upload", "Analytics", 'Settings', 'Contact'],
            icons=['house', 'cloud-upload', "graph-up-arrow", 'gear', 'phone'],
            menu_icon="cast",
            orientation="horizontal",
            styles={
                "nav-link": {
                    "text-align": "left",
                    "--hover-color": "#eee",
                }
            }
        )
        if selected == "Analytics":
            switch_page("Analytics")
        if selected == "Contact":
            switch_page("Contact")

html_page="""
<div style="width: 600px; padding: 50px;"</div>
<h1 style="border:3px solid Tomato; border-radius: 16px; text-align: center; text-shadow: 2px 2px 5px red; font-family: Arial;">  My Project</h1>
"""
st.markdown(html_page.format(),unsafe_allow_html=True)

st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")