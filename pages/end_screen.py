import streamlit as st
from pages import chai_style
from questionnaire_tools import log_answers

chai_style.render_title(256)
chai_style.render_chai_style()
st.divider()
log_answers(st.session_state)

st.title("Thank you!! :+1:")
st.image('https://www.chai-research.com/images/hero-slide-2.webp', width=512)
