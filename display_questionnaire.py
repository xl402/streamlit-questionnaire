import streamlit as st
from streamlit_sortables import sort_items

import numpy as np


GOAL_DESCRIPTION = "Please rank the AI responses based on how well it STAYS IN CHARACTER"


def display_rank_questionnaire(data):
    st.write("**Character's persona:**")
    st.write(data.get('persona'))
    st.write("**Conversation history:**")
    st.write(data.get('convo_history'))
    st.write(f"**{GOAL_DESCRIPTION}**")
    st.write('Higher up means better, bottom means worst')
    sorted_items = sort_items(data.get('responses'), direction='vertical')
    return sorted_items


def get_sampled_questionnaire_data(session_state):
    """
    Streamlit has session states that are persisted
    In this case, we do not want a re-sampling whenever the widgets state changes
    Hence we store them in unique session states as key-value pairs
    """
    if session_state not in st.session_state:
        data = _get_sampled_questionnaire_data()
        st.session_state[session_state] = data
    else:
        data = st.session_state[session_state]
    return data


def _get_sampled_questionnaire_data():
    data = {
        'persona': f'I am a {np.random.randint(100)} year old man',
        'convo_history': f'Bot: {np.random.randint(100)} year old',
        'responses': [str(np.random.randint(100)) for _ in range(3)]
    }
    return data
