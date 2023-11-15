import re

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from questionnaire_tools import QuestionBuilder
from pages import chai_style



def render_user_id_field():
    st.title("Enter your Chai user id")
    st.write('Your chai user id can be found in the setting section of the Chai app.')
    user_id = st.text_input("USER ID")
    return user_id


def render_next_page_button(user_id):
    if st.button("Next"):
        st.session_state['user_id'] = user_id
        switch_page("questionnaire_1")

def initialise_session_state():
    data = QuestionBuilder().build()
    st.session_state.update(data)

chai_style.render_title(256)
chai_style.render_chai_style()
st.divider()

initialise_session_state()
email = render_user_id_field()
render_next_page_button(email)
