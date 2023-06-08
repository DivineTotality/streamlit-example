import streamlit as st
from random import randint
from importlib import reload
from os import system
from time import sleep
l = 0
pts = 0
lib = 0
code = 0

st.title("CODE-IT-OUT!!")
st.divider()

def Question():
  global lib
  global pts
  global TrueUserInput
  if realOutput == 1:
    Question1 = (randint(1,1000))
    st.write("output the value of x as:", Question1)
    code = st.text_area("Code: ")
    
  elif realOutput == 2:
    QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
    st.write("Make a program that combines all these numbers,saved as x, y, z:", QuestionInput)
    code = st.text_area("Code: ")

st.write("P:", pts)
realOutput = (randint(1,2))
Question()
  
if st.button("Run"):
  code = str(code)
  exec(code)
  st.write("Why is:", x)

 
