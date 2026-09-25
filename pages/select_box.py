import streamlit as st

st.title("DropDown Selection")

course = st.selectbox(
    "Select Course",
    ["HTML","CSS","JAVASCRIPT","PYTHON"]
)

st.write("Selected Cpurse:",course)

