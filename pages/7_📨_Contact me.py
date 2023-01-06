from pathlib import Path
import streamlit as st  # pip install streamlit


current_dir= Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file=current_dir / "style" / "style.css"

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/florin_rot@yahoo.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
