import streamlit as st
from random import randint
from time import sleep

realOutput = (randint(1,2))
l = 0
pts = 0
lib = 0

class SessionState:
    def __init__(self):
        self.TrueUserInput = ""

state = SessionState()

def Writing():
    state.TrueUserInput = st.text_area("Code: ")
    if st.button("Submit"):
        st.code(state.TrueUserInput)

def HighScoreRecord():
    global pts
    HSR = open("HighScore.txt", "r")
    InterPTS = HSR.read()
    InterPTS = int(InterPTS)
    HSR.close()
    print('Current High Score:', InterPTS, "\n")

    if InterPTS <= pts:
        HS = open("HighScore.txt", "w")
        StringPTS = str(pts)
        HS.write(StringPTS)
        HS.close()
    else:
        return 0

def Question():
    global lib
    global pts
    if realOutput == 1:
        Question1 = (randint(1,1000))
        st.write("output the value of x as:", Question1)
        Writing()
    elif realOutput == 2:
        QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
        st.write("Make a program that combines all these numbers, saved as x, y, z:", QuestionInput)
        Writing()

    sleep(0.5)

def Checker():
    global lib
    global pts
    global Question1
    global QuestionInput
    if realOutput == 1:
        if state.TrueUserInput.x == Question1:
            print("\nCorrect!\n")
            print("P:", pts, "+ 100")
            pts += 100
            sleep(1)
        else:
            print("\nIncorrect!\n")
            print("P:", pts)
            sleep(1)
    elif realOutput == 2:
        if state.TrueUserInput.x + state.TrueUserInput.y + state.TrueUserInput.z == QuestionInput[0] + QuestionInput[1] + QuestionInput[2]:
            print("\nCorrect\n")
            print("P:", pts, "+ 150")
            pts += 150
            sleep(1)
        else:
            print("\nIncorrect!\n")
            print("P:", pts)
            sleep(1)

st.title("Code-It-Out!!")
st.divider()
Question()
