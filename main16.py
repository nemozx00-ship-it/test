#python -m streamlit run main16.py
import streamlit as st
import pandas as pd

file_path = 'score.csv'
data = pd.read_csv(file_path, skipinitialspace=True)
data.columns = data.columns.str.strip()
st.subheader("Bảng điểm")
st.dataframe(data)
data_copy = data.copy()
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'toan'] += 2
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'anh'] += 1
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'van'] += 2
st.subheader("Bảng điểm đã cộng ")
st.dataframe(data_copy)
