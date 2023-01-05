import streamlit as st


st.set_page_config(page_title="Contact me", page_icon="✉️")
st.title('Contact me')

form = st.form("my_form")
form.text_input('📩 Your email address',width=10)
form.text_input('📨 Sent email address')
form.text_input('📬 Subject')
form.text_area('📝 Description Email')

# Now add a submit button to the form:
form.form_submit_button("Submit")
