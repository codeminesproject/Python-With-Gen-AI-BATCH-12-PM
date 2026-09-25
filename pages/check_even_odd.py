


import streamlit as st

st.title("Check Even Odd: ")

number = st.text_input("Please Enter Number: ")

if st.button("Check"):
    int_num = int(number)
    if int_num%2==0:
        st.write("Number is even")
    else:
        st.write("Number is odd")
