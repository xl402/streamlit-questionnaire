import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from display_questionnaire import display_rank_questionnaire, get_sampled_questionnaire_data
from pages import chai_style

chai_style.render_title(256)
chai_style.render_chai_style()

st.title("Question 4 out of 4")

session_state = 'question_4'
data = get_sampled_questionnaire_data(session_state)
sorted_items = display_rank_questionnaire(data, session_state)

if st.button("**Next**"):
    switch_page("end_screen")
