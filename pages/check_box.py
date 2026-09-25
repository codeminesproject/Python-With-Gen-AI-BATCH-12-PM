import streamlit as st

st.title("Checkbox Selection")

agree = st.checkbox("I accept terms and conditions")

if agree:
    st.write("Thank you for selection")

