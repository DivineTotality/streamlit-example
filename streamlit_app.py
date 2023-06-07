from importlib import reload
from os import system
from time import sleep
realOutput = (randint(1,2))

realOutput = randint(1, 2)
l = 0
pts = 0
lib = 0
@@ -14,8 +15,9 @@ def Writing():
  TrueUserInput = st.text_area("Code: ")
  if st.button("Submit"):
    st.code(TrueUserInput)
    with open('TrueUserInput.py', 'w') as file_obj: # open function with 'w' argument it is mean you will add some text in empty file
    with open('TrueUserInput.py', 'w') as file_obj:
      file_obj.write(str(TrueUserInput))
    file_obj.close()


def HighScoreRecord():
@@ -25,26 +27,26 @@ def HighScoreRecord():
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
    Question1 = randint(1, 1000)
    st.write("output the value of x as:", Question1)
    Writing()
    

  elif realOutput == 2:
    QuestionInput =[(randint(0,999)), (randint(1,999)), (randint(1,999))]
    QuestionInput = [(randint(0, 999)), (randint(1, 999)), (randint(1, 999))]
    st.write("Make a program that combines all these numbers, saved as x, y, z:", QuestionInput)
    Writing()

@@ -66,16 +68,16 @@ def Checker():
      print("\nIncorrect!\n")
      print("P:", pts)
      sleep(1)
  elif realOutput==2:
    if TrueUserInput.x+TrueUserInput.y+TrueUserInput.z == QuestionInput[0]+QuestionInput[1]+QuestionInput[2]:
  elif realOutput == 2:
    if TrueUserInput.x + TrueUserInput.y + TrueUserInput.z == QuestionInput[0] + QuestionInput[1] + QuestionInput[2]:
      print("\nCorrect\n")
      print("P:", pts, "+ 150")
      pts += 150
      sleep(1)
    else:
      print("\nIncorrect!\n")
      print("P:", pts)
      sleep(1) 
      sleep(1)

st.title("Code-It-Out!!")
st.divider()
