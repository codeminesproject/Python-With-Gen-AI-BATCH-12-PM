import streamlit as st

st.title("DropDown Selection")

gender = st.radio(
    "Select Gender",
    ["Male","Female"]
)

st.write("Selected Gender:",gender)

