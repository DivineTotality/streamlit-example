import streamlit as st

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
    Writing()
    
  elif realOutput == 2:
    QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
    st.write("Make a program that combines all these numbers, saved as x, y, z:", QuestionInput)
    Writing()

  sleep(0.5)

def Checker():
  global lib
  global pts
  global TrueUserInput
  global Question1
  global QuestionInput
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

st.title("CODE-IT-OUT!!")
st.divider()
Question()

# Get the code input from the user
code = st.text_area("Enter your code here:", height=400)

# Execute the code
if st.button("Execute Code"):
  execute_code(code)
  Checker()
