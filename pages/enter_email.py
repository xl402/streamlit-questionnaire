# pages/Enter_Email.py
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Enter your email address")
email = st.text_input("Email")

if email:  # You should add proper validation for the email format
    if st.button("Next"):
        switch_page("questionnaire_1")
