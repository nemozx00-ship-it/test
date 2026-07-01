#python -m streamlit run main14.py
import streamlit as st
import pandas as pd
import random

st.title("📊 Quản lý Điểm số")
students = ["Kieu Vinh Khang", "Huyen Tan Khang", "Nguyen Minh Luan", "Ngo Bat Hieu"]
subjects = ["Toan", "Van", "Anh", "Khoa", "Sinh", "Su", "Dia", "GDCD", "Ly", "Tin hoc"]
csv_filename = "student.csv"
def luu_diem_moi():
    data = {
        "STT": [1, 2, 3, 4],
        "Hoc Sinh": students
    }
    for sub in subjects:
        data[sub] = [round(random.uniform(4.0, 10.0), 1) for _ in range(4)]
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
try:
    df_doc = pd.read_csv(csv_filename, encoding='utf-8-sig')
except FileNotFoundError:
    luu_diem_moi()
if st.button("🔄 Random dữ liệu", type="primary"):
    luu_diem_moi()
    st.rerun()
df_hien_thi = pd.read_csv(csv_filename, encoding='utf-8-sig')
st.dataframe(df_hien_thi, width="stretch", hide_index=True)
