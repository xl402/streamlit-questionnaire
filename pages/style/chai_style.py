import streamlit as st



def render_title(width, use_column_width=None):
    st.image(
            "https://www.chai-research.com/icons/chai-logo.svg",
            width=width,
            use_column_width=use_column_width,
            )

def hide_navbar():
    # We don't want users going back and forward across pages
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
            div[data-testid="collapsedControl"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


def hide_top_bar():
    page_bar = """
    <style>
    .css-18ni7ap {
    background: None;
    }
    </style>
    """
    st.markdown(page_bar, unsafe_allow_html=True)


def chai_bg_img():
    page_bg_img = """
    <style>
    .css-fg4pbf {
    background-image: url("https://images.typeform.com/images/zZZxfmch9bnt/background/large");
    background-size: cover;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


def next_button():
    next_button_style = """
    <style>
    .stButton>button {
        height: 25px;
        width: 150px;
        background-color: #EEEEEE;
        border: 2px solid #CCCCCC;
        border-radius: 5px;
    }
    </style>
    """
    st.markdown(next_button_style, unsafe_allow_html=True)


def render_chai_style():
    #hide_navbar()
    hide_top_bar()
    chai_bg_img()
    next_button()
