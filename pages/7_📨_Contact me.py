import streamlit as st

form_container = st.sidebar.container()
def get_customers():
    return [f'Customer {i+1}' for i in range(10)]

def submitted():
    st.session_state.submitted = True
def reset():
    st.session_state.submitted = False


if st.sidebar.button("Add User", on_click=reset):
    with form_container:
        with st.form("add user"):
            st.write("Add User")
            email = st.text_input("Email", key='new_email')
            customers = get_customers()
            customer = st.selectbox("Customer",customers, key='new_customer')
            password = st.text_input("Password", key='new_password')
            st.form_submit_button(label="Submit", on_click=submitted)
if 'submitted' in st.session_state:
    if st.session_state.submitted == True:
        print("Submit button pressed")
        new_user = {'email':st.session_state.new_email,
                     'customer':st.session_state.new_customer,
                     'password':st.session_state.new_password}
        st.sidebar.write(new_user)
        reset() # Prevents rerunning new user creation on next page load