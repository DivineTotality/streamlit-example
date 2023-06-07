import streamlit as st
from random import randint
from time import sleep

realOutput = randint(1, 2)
pts = 0
TrueUserInput = None

def Writing():
    global TrueUserInput
    TrueUserInput = st.text_area("Code: ")
    if st.button("Submit"):
        st.code(TrueUserInput)
        with open('UserInput.py', 'w') as file_obj:
            file_obj.write("code = '''\n")
            file_obj.write(TrueUserInput)
            file_obj.write("\n'''")

def HighScoreRecord():
    global pts
    HSR = open("HighScore.txt", "r")
    InterPTS = HSR.read()
    InterPTS = int(InterPTS)
    HSR.close()
    st.write('Current High Score:', InterPTS)

    if InterPTS <= pts:
        HS = open("HighScore.txt", "w")
        StringPTS = str(pts)
        HS.write(StringPTS)
        HS.close()
    else:
        return 0

def Question():
    global pts
    if realOutput == 1:
        Question1 = randint(1, 1000)
        st.write("Output the value of x as:", Question1)
        Writing()

        if st.button("Check Answer"):
            if TrueUserInput == str(Question1):
                st.write("Correct!")
                pts += 100
            else:
                st.write("Incorrect!")

    elif realOutput == 2:
        QuestionInput = [randint(0, 999), randint(1, 999), randint(1, 999)]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", QuestionInput)
        Writing()

        if st.button("Check Answer"):
            st.code(TrueUserInput)
            with open('TrueUserInput.py', 'w') as file_obj:
                file_obj.write("x = {}\n".format(QuestionInput[0]))
                file_obj.write("y = {}\n".format(QuestionInput[1]))
                file_obj.write("z = {}\n".format(QuestionInput[2]))

            try:
                exec(TrueUserInput)
                if 'x' in globals() and 'y' in globals() and 'z' in globals():
                    if x + y + z == sum(QuestionInput):
                        st.write("Correct!")
                        pts += 150
                    else:
                        st.write("Incorrect!")
                else:
                    st.write("Variables x, y, z are not defined.")
            except Exception as e:
                st.write("Error:", str(e))

st.title("Code-It-Out!!")
st.divider()
Question()
