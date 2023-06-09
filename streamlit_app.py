import streamlit as st
from random import randint
from time import sleep

QuestionChoices = randint(1, 2)
pts = 0
Question1 = 0
Question2 = [1, 2, 3]
current_question = None

def Question(QuestionChoices):
    global Question1
    global Question2
    global current_question
    if QuestionChoices == 1:
        current_question = Question1 = randint(1, 1000)
        st.write("output the value of x as:", Question1)
    elif QuestionChoices == 2:
        current_question = Question2 = [randint(0, 999), randint(1, 999), randint(1, 999)]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", Question2)

def is_current_question_answered():
    global current_question
    if current_question is None:
        return False
    if isinstance(current_question, int):
        return 'x' in locals()
    elif isinstance(current_question, list):
        return 'x' in locals() and 'y' in locals() and 'z' in locals()
    return False

def check_answer():
    global pts
    if current_question is None:
        return False
    if isinstance(current_question, int):
        if 'x' not in locals():
            return False
        if x == current_question:
            st.write("Correct!!")
            pts += 100
            st.session_state.result = "Correct"
        else:
            st.write("Wrong")
            st.session_state.result = "Wrong"
    elif isinstance(current_question, list):
        if 'x' not in locals() or 'y' not in locals() or 'z' not in locals():
            return False
        if x + y + z == sum(current_question):
            st.write("Correct!!")
            pts += 100
            st.session_state.result = "Correct"
        else:
            st.write("Wrong")
            st.session_state.result = "Wrong"

st.title("CODE-IT-OUT!!")
st.write("Points:", pts)
st.divider()

sleep(1)

if 'result' not in st.session_state:
    st.session_state.result = None

if 'QuestionChoices' not in st.session_state:
    st.session_state.QuestionChoices = QuestionChoices

if st.session_state.QuestionChoices != QuestionChoices:
    st.session_state.QuestionChoices = QuestionChoices
    st.session_state.result = None

Question(st.session_state.QuestionChoices)

form = st.form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

if submit:
    if is_current_question_answered():
        st.write("You have already answered the current question.")
    else:
        exec(code, globals(), locals())
        check_answer()

if st.session_state.result == "Correct":
    st.write("You answered correctly!")
elif st.session_state.result == "Wrong":
    st.write("You answered incorrectly!")
