#python -m streamlit run main17.py
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 1. Cấu hình trang Streamlit
st.set_page_config(
    page_title="Ứng dụng Xử lý & Làm sạch Dữ liệu", layout="wide"
)
st.title("📊 Ứng dụng Xử lý & Làm sạch Dữ liệu")

# 2. Tải dữ liệu (Ưu tiên File Uploader để tránh lỗi FileNotFoundError)
uploaded_file = st.file_uploader("Tải file CSV của bạn lên đây", type=["csv"])

# Bạn cũng có thể dùng đường dẫn file trong cùng thư mục:
# DEFAULT_PATH = "data5.6_1.csv"

if uploaded_file is not None:
    # Đọc dữ liệu
    df = pd.read_csv(uploaded_file)

    # Chuyển đổi các chuỗi "None" văn bản/khoảng trắng thành NaN thực sự
    df = df.replace(["None", "none", "NONE", "", " "], None)

    # ---------------------------------------------------------
    # YÊU CẦU 1: Hiển thị bản gốc & Thống kê
    # ---------------------------------------------------------
    st.subheader("1. Dữ liệu gốc")
    st.dataframe(df, use_container_width=True)

    # Đếm số dòng trùng lặp
    num_duplicates = df.duplicated().sum()
    st.info(
        f"📌 Số lượng dòng trùng lặp trong dữ liệu gốc: **{num_duplicates}** dòng."
    )

    # Đếm số lượng giá trị None/NaN ở từng cột bằng `df.isnull().sum()`
    st.write("🔍 **Thống kê số lượng giá trị None/NaN theo từng cột:**")
    st.write(df.isnull().sum())

    st.divider()

    # ---------------------------------------------------------
    # YÊU CẦU 2 & 3: Nút bấm tóm gọn (Xóa trùng & Xóa None)
    # ---------------------------------------------------------
    if st.button("🧹 Tóm gọn & Làm sạch dữ liệu", type="primary"):
        df_clean = df.copy()

        # 1. Xóa các dòng trùng lặp
        df_clean = df_clean.drop_duplicates()

        # 2. Xóa các dòng chứa giá trị None/NaN ở các cột
        columns_list = list(df_clean.columns)
        df_clean = df_clean.dropna(subset=columns_list)

        # Thông báo và hiển thị chỉ số so sánh
        st.success("✅ Đã xử lý làm sạch dữ liệu thành công!")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Số dòng ban đầu", len(df))
        with col2:
            st.metric("Số dòng sau khi làm sạch", len(df_clean))

        st.subheader("2. Dữ liệu sau khi làm sạch")
        st.dataframe(df_clean, use_container_width=True)

else:
    st.warning(
        "👈 Vui lòng tải file CSV lên ở bảng phía trên để bắt đầu xử lý!"
    )