import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages
from display_questionnaire import display_rank_questionnaire, get_sampled_questionnaire_data
from pages.style import chai_style

hide_pages(['Home Screen','Enter Email','End Screen'])

chai_style.render_title(256)
chai_style.render_chai_style()

st.title("Question 1 out of 4")

st.divider()
data = get_sampled_questionnaire_data('data_1')

sorted_items = display_rank_questionnaire(data)

# st.write(f'sorted_items: {sorted_items}')

if st.button("**Next**"):
    switch_page("Question 2")
