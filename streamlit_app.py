import streamlit as st

st.title("CODE-IT-OUT!!")
st.divider()

code = st.text_area("Code: ")

if st.button("Run"):
  exec(code)
  st.write("Why is:", x)

 
