#python -m streamlit run main17.py
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Xử lý Dữ liệu", layout="wide")
st.title("📊 Ứng dụng Xử lý & Làm sạch Dữ liệu")
FILE_PATH = r"C:\Users\Nhat Kieu\Desktop\New folder\hkd\data5.6_1.csv"
@st.cache_data
def load_data(path):
    return pd.read_csv(path)
try:
    df = load_data(FILE_PATH)
    df = df.replace(["None", "none", "NONE", "", " "], None)
    st.subheader("1. Dữ liệu gốc")
    st.dataframe(df, use_container_width=True)
    num_duplicates = df.duplicated().sum()
    st.info(
        f"📌 Số lượng dòng trùng lặp trong dữ liệu gốc: **{num_duplicates}** dòng."
    )
    st.write("🔍 **Thống kê số lượng giá trị None/NaN ở từng cột:**")
    st.write(df.isnull().sum())
    st.divider()
    if st.button("🧹 Tóm gọn & Làm sạch dữ liệu", type="primary"):
        df_clean = df.copy()
        df_clean = df_clean.drop_duplicates()
        columns_list = list(df_clean.columns)
        df_clean = df_clean.dropna(subset=columns_list)
        st.success("✅ Đã xử lý làm sạch dữ liệu thành công!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Số dòng ban đầu", len(df))
        with col2:
            st.metric("Số dòng sau khi làm sạch", len(df_clean))
        st.subheader("2. Dữ liệu sau khi làm sạch")
        st.dataframe(df_clean, use_container_width=True)
except FileNotFoundError:
    st.error(f"❌ Không tìm thấy file tại đường dẫn: `{FILE_PATH}`")