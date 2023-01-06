import streamlit as st


st.set_page_config(page_title="Contact me", page_icon="✉️")
st.title('Contact me')

contact_form="""
<form action="https://formsubmit.co/florin_rot@yahoo.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)