import streamlit as st


st.set_page_config(page_title="Contact me", page_icon="✉️")
st.title('Contact me')

contact_form="""
<form action="https://formsubmit.co/florin_rot@yahoo.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#use local css File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)



local_css("style/style.css")        