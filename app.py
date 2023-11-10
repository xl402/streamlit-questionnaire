import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages import chai_style


# Streamlit forces set page config to be called before any other Streamlit command
st.set_page_config(initial_sidebar_state="collapsed")

if __name__ == '__main__':
    chai_style.render_title(256)
    chai_style.render_chai_style()
    st.divider()

    st.title("WIN 1 YEAR UNLIMITED MESSAGES! Help us to make AI that STAY in Character 😇")
    st.header(
            "4 questions, rank model responses based on :blue[how well they stay in character] :thinking_face: ",
            )

    if st.button("**Start**"):
        switch_page("enter_email")
