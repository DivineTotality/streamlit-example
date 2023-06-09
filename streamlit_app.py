import streamlit as st
from random import randint

st.title("CODE-IT-OUT!!")

if 'pts' not in st.session_state:
    st.session_state['pts'] = 0

def generate_question():
    question_choices = randint(1, 2)
    question1 = 0
    question2 = []

    if question_choices == 1:
        question1 = randint(1, 1000)
        st.write("Output the value of x as:", question1)
        return question_choices, question1
    elif question_choices == 2:
        question2 = [randint(0, 999), randint(1, 999), randint(1, 999)]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", question2)
        return question_choices, question2

question_choices, question = generate_question()

form = st.form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

if submit:
    result = False
    if question_choices == 1:
        exec(code, globals())
        if 'x' in globals() and x == question:
            result = True
    elif question_choices == 2:
        exec(code, globals())
        if 'x' in globals() and 'y' in globals() and 'z' in globals() and x + y + z == sum(question):
            result = True
    
    if result:
        st.write("**Correct!!**")
        st.session_state['pts'] += 100
    else:
        st.write("**Wrong**")

    # Generate a new question
    question_choices, question = generate_question()

st.write("Points:", st.session_state['pts'])
st.divider()
