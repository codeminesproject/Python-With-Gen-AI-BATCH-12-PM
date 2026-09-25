


import streamlit as st

st.title("Login Form: ")

username = st.text_input("Please Enter Username: ")
password = st.text_input("Please Enter Password: ",type="password")

if st.button("Login"):
    if username=="admin" and password=="pass@123":
        st.success("Login Successfull")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid Login")
