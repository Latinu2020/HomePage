import streamlit as st

if __name__=='__main__':

        with st.form("Email Form"):
            subject =st.text_input(label='Subject',placeholder="Please enter subject of your mail")
            fullName =st.text_input(labe='Full Name', placeholder="PLease enter your full name")
            email=st.text_input(label='Email Address', placeholder= "Please enter your email address")
            text =st.text_area(label='Email Text', placeholder="PLease enter your text here")
            uploaded_file=st.file_uploader("Attachment")
            submit_res= st.form_submit_button(label='Send')

