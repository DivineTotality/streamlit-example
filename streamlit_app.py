import streamlit as st
from random import randint
from time import sleep

QuestionChoices = randint(1, 2)
pts = 0
Question1 = 0
Question2 = [1, 2, 3]

def Question(QuestionChoices):
    global Question1
    global Question2
    if QuestionChoices == 1:
        Question1 = randint(1, 1000)
        st.write("output the value of x as:", Question1)
    elif QuestionChoices == 2:
        Question2 = [randint(0, 999), randint(1, 999), randint(1, 999)]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", Question2)

st.title("CODE-IT-OUT!!")
st.write("Points:", pts)
st.divider()

sleep(1)

Question(QuestionChoices)

form = st.form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

@st.cache
def execute_code(code):
    exec(code, globals(), locals())

if 'result' not in st.session_state:
    st.session_state.result = None

if submit:
    if QuestionChoices == 1:
        execute_code(code)
        if 'x' in locals():
            st.code(x)
            if x == Question1:
                st.write("Correct!!")
                pts += 100
                st.session_state.result = "Correct"
            else:
                st.write("Wrong")
                st.session_state.result = "Wrong"
        else:
            st.write("Variable 'x' not defined")
    elif QuestionChoices == 2:
        execute_code(code)
        if 'x' in locals() and 'y' in locals() and 'z' in locals():
            st.code(x + y + z)
            if x + y + z == sum(Question2):
                st.write("Correct!!")
                pts += 100
                st.session_state.result = "Correct"
            else:
                st.write("Wrong")
                st.session_state.result = "Wrong"
        else:
            st.write("Variables 'x', 'y', 'z' not defined")

if st.session_state.result == "Correct":
    st.write("You answered correctly!")
elif st.session_state.result == "Wrong":
    st.write("You answered incorrectly!")
