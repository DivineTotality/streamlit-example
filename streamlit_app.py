import streamlit as st

def exec_code(code):
  """Executes the given code."""
  exec(code)

def main():
  """Main function."""
  code = st.text_area("Enter code:")
  if st.button("Execute"):
    exec_code(code)
    st.write(y)

if __name__ == "__main__":
  main()
