from questionnaire_tools import QuestionBuilder
import pandas as pd


def test_data_sampler():
    df = pd.read_feather('data.ftr')

    sampler = QuestionBuilder(number_of_questions=4)
    out = sampler.build()

    assert set(out.keys()) == {'question_1', 'question_2', 'question_3', 'question_4'}

    for data in out.values():
        assert data.keys() == {'conversation_id', 'persona', 'conversation', 'responses', 'captcha'}

        ix = (df['conversation_id'] == data['conversation_id']).values
        row = df[ix].to_dict(orient='records')[0]
        assert data['conversation'] == row['sampled_text']

        expected_responses = [row[f'sample_response_{i}'] for i in range(1, 4)]
        if not data['captcha']:
            assert data['responses'] == expected_responses
        else:
            assert len(set(expected_responses).intersection(data['responses'])) == 1


    # check there is only 1 captcha
    captchas = [x['captcha'] for x in out.values()]
    assert sorted(captchas)[:3] == [0, 0, 0]
    assert sorted(captchas)[-1] > 0
