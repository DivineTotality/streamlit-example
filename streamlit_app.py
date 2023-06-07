import streamlit as st

def execute_code(code):
  try:
    exec(code)
  except Exception as e:
    st.error(e)

st.title("Code Execution App")

# Get the code input from the user
code = st.text_area("Enter your code here:", height=400)

# Execute the code
if st.button("Execute Code"):
  st.write(exec(code))
