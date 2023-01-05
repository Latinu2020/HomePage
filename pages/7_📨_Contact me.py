from pathlib import Path
import streamlit as st


current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file=current_dir / "styles" / "style.css"
with open(css_file) as f:
    form = st.form("my_form")
    form.text_input('Your email address',"<style>{}</style".format(f.read()), unsafe_allow_html=True)
    form.text_input('Sent email address',"<style>{}</style".format(f.read()), unsafe_allow_html=True)
    form.text_input('Subject',"<style>{}</style".format(f.read()), unsafe_allow_html=True)
    form.text_area('Description Email',"<style>{}</style".format(f.read()), unsafe_allow_html=True)

# Now add a submit button to the form:
    form.form_submit_button("Submit")
