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
        with open('TrueUserInput.py', 'w') as file_obj:
            file_obj.write("x = {}\n".format(TrueUserInput))

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
  global TrueUserInput
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
    global pts
    global TrueUserInput
    if realOutput == 1:
        if TrueUserInput == str(Question1):
            st.write("Correct!")
            pts += 100
        else:
            st.write("Incorrect!")
    elif realOutput == 2:
        if 'x' in globals():
            x_value = globals()['x']
            if x_value == sum(QuestionInput):
                st.write("Correct!")
                pts += 150
            else:
                st.write("Incorrect!")
        else:
            st.write("Variable x is not defined.")

st.title("Code-It-Out!!")
st.divider()
Question()
