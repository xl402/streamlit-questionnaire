import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from questionnaire_tools import display_page
from pages import chai_style

chai_style.render_title(256)
chai_style.render_chai_style()

display_page(question_number=3)
