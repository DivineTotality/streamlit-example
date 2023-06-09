import streamlit as st
from random import randint
from time import sleep

st.title("CODE-IT-OUT!!")

if 'pts' not in st.session_state:
    st.session_state['pts'] = 0

QuestionChoices = randint(1, 2)
Question1 = 0
Question2 = {1, 2, 3}

def Question(QuestionChoices):
    global Question1
    global Question2
    if QuestionChoices == 1:
        Question1 = (randint(1, 1000))
        st.write("output the value of x as:", Question1)
    elif QuestionChoices == 2:
        Question2 = [(randint(0, 999)), (randint(1, 999)), (randint(1, 999))]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", Question2)

result_placeholder = st.empty()
Question(QuestionChoices)

form = st.form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

if submit:
    if QuestionChoices == 1:
        exec(code)
        st.code(x)
        if x == Question1:
            result_placeholder.write("Correct!!")
            st.session_state['pts'] += 100
        else:
            result_placeholder.write("Wrong")
    elif QuestionChoices == 2:
        exec(code)
        st.code(x + y + z)
        if x + y + z == Question2[0] + Question2[1] + Question2[2]:
            result_placeholder.write("Correct!!")
            st.session_state['pts'] += 100
        else:
            result_placeholder.write("Wrong")

st.write("Points:", st.session_state['pts'])
st.divider()
