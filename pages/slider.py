import streamlit as st

st.title("Slider Example")

duration = st.slider("Duration in months:",12,90)

st.write("Selected Duration: ",duration)

