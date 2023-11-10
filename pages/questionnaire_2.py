import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from display_questionnaire import display_rank_questionnaire, get_sampled_questionnaire_data

st.title("Question 2 out of 4")

data = get_sampled_questionnaire_data('data_2')

sorted_items = display_rank_questionnaire(data)

st.write(f'sorted_items: {sorted_items}')


if st.button("Next"):
    switch_page("end_screen")
