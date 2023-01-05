import streamlit as st

with open('style/style.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

form = st.form("my_form")
form.text_input('Your email address')
form.text_input('Sent email address')
form.text_input('Subject')
form.text_area('Description Email')

# Now add a submit button to the form:
form.form_submit_button("Submit")
