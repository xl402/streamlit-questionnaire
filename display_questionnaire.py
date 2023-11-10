import streamlit as st
from streamlit_sortables import sort_items


def display_rank_questionnaire(persona, convo_history, responses):
    st.write("**Character's persona:**")
    st.write(persona)
    st.write("**Conversation history:**")
    st.write(convo_history)
    st.write("**Please rank responses (higher up is better)**")
    sorted_items = sort_items(responses, direction='vertical')
    return sorted_items
