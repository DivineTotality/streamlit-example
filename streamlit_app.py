import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from importlib import reload
from os import system
from time import sleep
realOutput = (randint(1,2))
l = 0
pts = 0
lib = 0


def execute_code(code):
  try:
    exec(code)
  except Exception as e:
    st.error(e)
    
def Question():
  global lib
  global pts
  global TrueUserInput
  if realOutput == 1:
    Question1 = (randint(1,1000))
    st.write("output the value of x as:", Question1)
    code = st.text_area("Enter your code here:", height=400)
    
  elif realOutput == 2:
    QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
    st.write("Make a program that combines all these numbers, saved as x, y, z:", QuestionInput)
    code = st.text_area("Enter your code here:", height=400)

  sleep(0.5)

st.title("CODE-IT-OUT!!")
st.divider()
Question()

# Execute the code
if st.button("Execute Code"):
  execute_code(code)
  Checker()
