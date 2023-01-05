from pathlib import Path
import streamlit as st


current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file=current_dir / "styles" / "style.css"
with open(css_file) as f:
    st.text_area("<style>{}</style".format(f.read()), unsafe_allow_html=True)

form = st.form("my_form")
form.text_input('Your email address')
form.text_input('Sent email address')
form.text_input('Subject')
form.text_area('Description Email')

# Now add a submit button to the form:
form.form_submit_button("Submit")
