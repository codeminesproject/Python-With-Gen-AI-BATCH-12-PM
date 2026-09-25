import streamlit as st
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\BATCH 12\\student_data_1.xlsx")

st.dataframe(df)