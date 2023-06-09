import streamlit as st
from random import randint
from time import sleep
QuestionChoices = randint(1,2)
pts = 0

st.title("CODE-IT-OUT!!")
st.write("Points:", pts)
st.divider()

sleep(1)

if QuestionChoices == 1:
  Question1 = (randint(1,1000))
  st.write("output the value of x as:", Question1)
elif QuestionChoices == 2:
  Question2 =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
  st.write("Make a program that combines all these numbers,saved as x, y, z:", Question2)

  
form = form(key='my-form')
code = form.text_area("Code:")
submit = form.form_submit_button("Run")

if submit:
  if QuestionChoices == 1:
    exec(code)
    st.code(x)
    if x == Question1:
      st.write("Correct!!")
      pts+=100
    else:
      st.write("Wrong")
  elif QuestionChoices == 2:
    exec(code)
    st.code(x+y+z)
    if x+y+z == Question2[0] + Question2[1] + Question2[2]:
      st.write("Correct!!")
      pts+=100
    else:
      st.write("Wrong")
