from streamlit_extras.switch_page_button import switch_page
from streamlit_sortables import sort_items
import numpy as np
import pandas as pd
import streamlit as st


GOAL_DESCRIPTION = "Please rank (drag and drop) the AI responses based on how well it STAYS IN CHARACTER"
NUMBER_OF_QUESTIONS = 4

def display_page(question_number):
    session_state = f'question_{question_number}'
    st.title(f"Question {question_number} out of {NUMBER_OF_QUESTIONS}")
    sorted_items = display_rank_questionnaire(session_state)

    if question_number < NUMBER_OF_QUESTIONS:
        next_page = f'questionnaire_{question_number + 1}'
    else:
        next_page = "end_screen"

    if st.button("**Next**"):
        switch_page(next_page)


def display_rank_questionnaire(session_state):
    data = st.session_state.to_dict().get(session_state)
    if data:
        st.write("**Character's persona:**")
        st.write(data.get('persona'))
        st.write("**Conversation history:**")
        st.write(data.get('conversation'))
        st.subheader(f"**{GOAL_DESCRIPTION}**")
        st.write('Higher up means better, bottom means worse')
        sorted_items = sort_items(data.get('responses'), direction='vertical')
        st.session_state[session_state]['ordered_responses'] = sorted_items
        return sorted_items


def log_answers(session_state):
    state = session_state.to_dict()
    #TODO: LOG ON GUANACO


class QuestionBuilder:

    def __init__(self, number_of_questions=NUMBER_OF_QUESTIONS, data_path='data.ftr'):
        self.number_of_questions = NUMBER_OF_QUESTIONS
        self.df = pd.read_feather(data_path)


    def build(self):
        raw_data = self._load_sample()
        captcha = np.random.randint(self.number_of_questions)
        data = {}
        for i, row in enumerate(raw_data):
            is_captcha_question = captcha == i
            data[f'question_{i + 1}'] = self._format(row, is_captcha_question)
        return data

    def _load_sample(self):
        raw_data = self.df.sample(self.number_of_questions).to_dict(orient='records')
        return raw_data

    def _format(self, row, is_captcha_question):
        responses = [row[f'sample_response_{i}'] for i in range(1, 4)]
        if is_captcha_question:
            correct_response = np.random.choice(responses)
            random_responses = self._sample_responses(row['conversation_id'], n_responses=2)
            random_responses = [correct_response] + random_responses
            correct_answer_position = np.random.randint(3)
            responses = random_responses[:]
            responses[correct_answer_position] = random_responses[0]
            responses[0] = random_responses[correct_answer_position]

        question = {
            'conversation_id': row['conversation_id'],
            'persona': row['persona'],
            'conversation': row['sampled_text'],
            'responses': responses,
            'captcha': 0 if not is_captcha_question else correct_answer_position
        }
        return question

    def _sample_responses(self, convo_id_to_exclude, n_responses):
        ix = (self.df['conversation_id'] != convo_id_to_exclude).values
        df = self.df[ix]
        ns = np.random.randint(1, 4, n_responses)
        df = df.sample(n_responses)
        return [row[f'sample_response_{n}'] for n, (_, row) in zip(ns, df.iterrows())]


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
    return data
