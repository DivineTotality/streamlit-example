import streamlit as st

def execute_code(code):
  """Executes the given code in the current Python environment.

  Args:
    code: The code to execute.

  Returns:
    The value of the last expression evaluated in the code.
  """
  exec(code)

st.title("Code Execution")

# Get the code from the user.
code = st.text_area("Enter your code:")

# Execute the code and print the result.
if st.button("Run"):
  result = execute_code(code)
  st.write("The result is:", result)
