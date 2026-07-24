#python -m streamlit run main16.py
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

csv_content = """ho ten, toan, anh, van
vinh khang, 8, 9, 8
luan, 9, 7, 8
phu, 7, 9, 8
tan khang, 9, 7, 10"""
try:
    with open("C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\score.csv", "x", encoding="utf-8") as f:
        f.write(csv_content)
except FileExistsError:
    pass
df_original = pd.read_csv("C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\score.csv")
df_original.columns = [c.strip() for c in df_original.columns]
df_updated = df_original.copy()
mask = df_updated["ho ten"].str.strip().str.lower() == "vinh khang"
df_updated.loc[mask, ["toan", "anh", "van"]] = 10
st.subheader("1. Bảng điểm ban đầu")
st.dataframe(df_original, use_container_width=True)
st.divider()
st.subheader("2. Bảng điểm sau khi cộng điểm (Vinh Khang = 10)")
st.dataframe(df_updated, use_container_width=True)

