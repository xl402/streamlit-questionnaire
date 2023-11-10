import streamlit as st
from pages import chai_style


chai_style.render_title(256)
chai_style.render_chai_style()
st.divider()

st.title("Thank you!! :+1:")
st.image('https://www.chai-research.com/images/hero-slide-2.webp', width=512)
