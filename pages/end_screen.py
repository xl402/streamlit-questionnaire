import streamlit as st
from pages.style import chai_style

chai_style.hide_navbar()
chai_style.render_title(256)
chai_style.render_chai_style()
st.divider()

st.title("Thank you!! :gift_heart:")
st.image('https://www.chai-research.com/images/hero-slide-2.webp', width=512)
