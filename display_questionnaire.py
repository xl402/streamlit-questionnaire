from streamlit_sortables import sort_items
import numpy as np
import pandas as pd
import streamlit as st


GOAL_DESCRIPTION = "Please rank (drag and drop) the AI responses based on how well it STAYS IN CHARACTER"


def display_rank_questionnaire(data, session_state):
    st.write("**Character's persona:**")
    st.write(data.get('persona'))
    st.write("**Conversation history:**")
    st.write(data.get('convo_history'))
    st.subheader(f"**{GOAL_DESCRIPTION}**")
    st.write('Higher up means better, bottom means worse')
    sorted_items = sort_items(data.get('responses'), direction='vertical')
    st.session_state[session_state]['ordered_responses'] = sorted_items
    return sorted_items


def log_answers(session_state):
    state = session_state.to_dict()
    #TODO: LOG ON GUANACO


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
    # inefficient? yes. but it's a demo
    df = pd.read_feather('data.ftr')
    raw_data = df.sample().to_dict(orient='records')[0]
    data = {
        'persona': raw_data['persona'],
        'convo_history': raw_data['sampled_text'],
        'responses': [raw_data[f'sample_response_{i}'] for i in range(1, 4)]
    }
    data = {'persona': 'He is a bot', 'convo_history': 'yo', 'responses': ['A', 'B', 'C', 'D']}
    return data
