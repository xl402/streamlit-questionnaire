import re

import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def render_email_field():
    st.title("Enter your email address")
    email = st.text_input("Email")
    return email


def render_next_page_button(email):
    if st.button("Next") and email_entered_correctly(email):
        switch_page("questionnaire_1")


def email_entered_correctly(email):
    if email is None or not _email_address_is_valid(email.lower()):
        st.error("Please enter a valid email address")
        return False
    return True


def _email_address_is_valid(email_address):
   match = re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email_address)
   return bool(match)


email = render_email_field()
render_next_page_button(email)
