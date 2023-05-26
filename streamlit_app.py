import streamlit as st


st.title("Code-It-Out!!")
UserInput = st.text_input("Code: ")
st.code(UserInput)

