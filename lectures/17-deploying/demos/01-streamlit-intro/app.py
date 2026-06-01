import streamlit as st

st.title("Number Doubler")

number = st.number_input("Enter a number", value=0)

doubled = number * 2

st.write(f"{number} doubled is {doubled}.")
