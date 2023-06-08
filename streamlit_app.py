import streamlit as st

code = st.text_area("Code: ")

if st.button("Run"):
  exec(code)
  st.write("Why is:", x)
