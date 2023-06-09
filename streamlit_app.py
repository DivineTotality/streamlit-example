import streamlit as st
from random import randint

st.title("CODE-IT-OUT!!")

if 'pts' not in st.session_state:
    st.session_state['pts'] = 0

question_choices = randint(1, 2)
question1 = 0
question2 = []

def generate_question():
    global question1
    global question2
    
    if question_choices == 1:
        question1 = randint(1, 1000)
        st.write("Output the value of x as:", question1)
    elif question_choices == 2:
        question2 = [randint(0, 999), randint(1, 999), randint(1, 999)]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", question2)

def check_answer(code):
    if question_choices == 1:
        exec(code, globals())
        if 'x' in globals() and x == question1:
            return True
        else:
            return False
    elif question_choices == 2:
        exec(code, globals())
        if 'x' in globals() and 'y' in globals() and 'z' in globals() and x + y + z == sum(question2):
            return True
        else:
            return False

form = st.form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

if submit:
    result = check_answer(code)
    
    if result:
        st.write("**Correct!!**")
        st.session_state['pts'] += 100
    else:
        st.write("**Wrong**")

    # Generate a new question
    question_choices = randint(1, 2)
    generate_question()

st.write("Points:", st.session_state['pts'])
st.divider()
