#python -m streamlit run main17.py
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

file_path = 'C:\\Users\\Nhat Kieu\\Desktop\\New folder\\New folder\\score.csv'
data = pd.read_csv(file_path, skipinitialspace=True)
data.columns = data.columns.str.strip()
st.subheader("Bảng điểm")
st.dataframe(data)
data_copy = data.copy()
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'toan'] += 2
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'anh'] += 1
data_copy.loc[data_copy['ho ten'] == 'vinh khang', 'van'] += 2
st.subheader("Bảng điểm Đã cộng điểm")
st.dataframe(data_copy)

