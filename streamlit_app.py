import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from importlib import reload
from os import system
from time import sleep
l = 0
pts = 0
lib = 0

def Writing():
  PATH_TO_MY_FILE = './TrueUserInput.py'
  UserInput = st.text_area("Code: ")
  f = open("TrueUserInput.py", "w")
  f.write(UserInput)
  f.close()
  st.code(UserInput)
  writeToFile(PATH_TO_MY_FILE, UserInput)


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

def Checker():
  global lib
  global pts
  global TrueUserInput
  if realOutput == 1:
    Question1 = (randint(1,1000))
    print("output the value of x as:", Question1)
    Writing()
    
  elif realOutput == 2:
    QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
    print("Make a program that combines all these numbers,saved as x, y, z:", QuestionInput)
    Writing()

  sleep(0.5)
  if lib==0:
    import TrueUserInput
    lib=1
  else:
    reload(TrueUserInput)

  if realOutput == 1:
    if TrueUserInput.x == Question1:
      print("\nCorrect!\n")
      print("P:", pts, "+ 100")
      pts += 100
      sleep(1)
    else:
      print("\nIncorrect!\n")
      print("P:", pts)
      sleep(1)
  elif realOutput==2:
    if TrueUserInput.x+TrueUserInput.y+TrueUserInput.z == QuestionInput[0]+QuestionInput[1]+QuestionInput[2]:
      print("\nCorrect\n")
      print("P:", pts, "+ 150")
      pts += 150
      sleep(1)
    else:
      print("\nIncorrect!\n")
      print("P:", pts)
      sleep(1) 

st.write('Code will be executed and printed')
st.title("Code-It-Out!!")   
Writing()
 
with st.echo():
  print("Yes")
