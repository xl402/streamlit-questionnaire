import streamlit as st
from streamlit_extras.switch_page_button import switch_page


# Streamlit forces set page config to be called before any other Streamlit command
st.set_page_config(initial_sidebar_state="collapsed")


def hide_navbar():
    # We don't want users going back and forward across pages
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


if __name__ == '__main__':
    hide_navbar()
    st.title("WIN 1 YEAR UNLIMITED MESSAGES!")
    st.header("Help us to make AI that STAY in Character 😇")
    st.title('4 questions, rank model responses based on how well they stay in character')

    if st.button("Next"):
        switch_page("enter_email")
