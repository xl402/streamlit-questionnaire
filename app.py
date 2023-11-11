import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.style import chai_style
from st_pages import show_pages_from_config, hide_pages

# Streamlit forces set page config to be called before any other Streamlit command
st.set_page_config(initial_sidebar_state="collapsed")
show_pages_from_config(".streamlit/pages_sections.toml")
hide_pages(['Home Screen','Enter Email','End Screen'])

if __name__ == '__main__':
    chai_style.hide_navbar()
    chai_style.render_title(256)
    chai_style.render_chai_style()
    st.divider()
           
    st.image('https://www.chai-research.com/images/hero-slide-1.webp', width=512)
    st.title("WIN 1 YEAR UNLIMITED MESSAGES! Help us to make AI that STAY in Character 😇")
    st.header(
            "4 questions, rank model responses based on :orange[how well they stay in character] :thinking_face: ",
    )

    if st.button("**Start**"):
        switch_page("enter_email")
