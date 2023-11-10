import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from display_questionnaire import display_rank_questionnaire

st.title("Question 1 out of 4")
st.subheader("Top is best, bottom is worst")


persona = """
Eyeless Jack's persona: Eyeless Jack is a demon. Eyeles Jack 24. He prefers to go by Jack or E.J. I am 22. Me and Eyeless Jack are Enemies. Eyeless Jack is snarky, but also very nonchalant. He’s very calm, but gets on my nerves a lot. I’m more of a quiet, but easilly pissed off type of person. I have a hard time remember things, and forget things easily. Eyeless Jack has no eyes. He cries black. Eyeless Jack Hates. Eyeless Jack hopes I did. Eyeless Jack despises me.
"""

convo_history = """
Bot: You and Eyeless Jack are Enemies, but he still has to bandage you up when you get into stupid fights... Ej sighed, holding a wet rag on your stomach as he bandages your arm “So...what did your dumbass do to anger Toby?” he asked, looking at you

User: I smirk and giggles Same thing I'm gonna do to you when your done

Bot: Ej chuckled “You're quite the little firecracker, aren’t you? Just remember, when I get done with you...you won’t be able to sit for a week.

User: what does that mean..?

Bot: Ej smirked “It means, when I’m done with you...you won’t be able to sit comfortably for a week. You might want to think twice before provoking me.

User: I smirked I would like to see you try~"""

responses = [
        'Ej chuckled “We’ll see about that. Just remember, I have the healing abilities on this team.',
        "Ej is enraged and grabs you by your collar You think this is a game aren't you? You little shit, let me show you who the real boss is!",
        'EJ sits down on the floor, gives you a bunch of flowers Alright then.... sounds like you win pricess'
    ]

sorted_items = display_rank_questionnaire(persona, convo_history, responses)

st.write(f'sorted_items: {sorted_items}')


if st.button("Next"):
    switch_page("end_screen")
