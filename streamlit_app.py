import streamlit as st
from random import randint
from os import system
QuestionChoices = randint(1,2)
pts = 0

st.title("CODE-IT-OUT!!")
st.write("Points:", pts)
st.divider()

if QuestionChoices == 1:
  Question1 = (randint(1,1000))
  st.write("output the value of x as:", Question1)
elif QuestionChoices == 2:
  Question2 =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
  print("Make a program that combines all these numbers,saved as x, y, z:", Question2)

code = st.text_area("Code: ")

if st.button("Run"):
  if QuestionChoices == 1:
    exec(code)
    st.code(x)
  elif QuestionChoices == 2:
    exec(code)
    st.code(x+y+z)

  if QuestionChoices == 1:
    if x == Question1:
      st.write("Correct!!")
      pts+=100
    else:
      st.write("Wrong")
  elif QuestionChoices == 2:
    if x+y+z == Question2[0] + Question2[1] + Question[2]:
      st.write("Correct!!")
      pts+=100
    else:
      st.write("Wrong")
