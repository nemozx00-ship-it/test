#python -m streamlit run main18.py
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Phép Tính Thống Kê", layout="wide")
uploaded_file = st.file_uploader(
    "Tải file CSV của bạn lên đây (ví dụ: data5.8.csv)", type=["csv"])
def tinh_va_hien_thi_chi_tiet(series_data, ui_container):
    col_clean = pd.to_numeric(series_data, errors="coerce").dropna()
    arr = col_clean.tolist()
    n = len(arr)
    with ui_container:
        st.subheader(f"📌 {series_data.name}")
        if n == 0:
            st.warning("Không có dữ liệu số để tính toán!")
            return
        max_val = arr[0]
        min_val = arr[0]
        for x in arr:
            if x > max_val:
                max_val = x
            if x < min_val:
                min_val = x
        st.write(
            f"📈 **Max:** `{max_val}` *(So sánh tìm giá trị lớn nhất trong {n} phần tử)*")
        st.write(
            f"📉 **Min:** `{min_val}` *(So sánh tìm giá trị nhỏ nhất trong {n} phần tử)*")
        tong = sum(arr)
        mean_val = tong / n
        st.write(
            f"📊 **Mean:** `{mean_val:.2f}`"
            f"<br>&nbsp;&nbsp;&nbsp;&nbsp;👉 *Phép tính:* $\\frac{{\\text{{Tổng}}}}{{\\text{{Số lượng}}}} = \\frac{{{tong:,.2f}}}{{{n}}} = {mean_val:.2f}$",
            unsafe_allow_html=True,)
        arr_sorted = list(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr_sorted[j] > arr_sorted[j + 1]:
                    arr_sorted[j], arr_sorted[j + 1] = (
                        arr_sorted[j + 1],
                        arr_sorted[j],)
        if n % 2 == 1:
            idx = n // 2
            median_val = arr_sorted[idx]
            phep_tinh_median = f"Số phần tử là **lẻ** ($N = {n}$), lấy vị trí chính giữa $({idx + 1})$ $\\rightarrow$ `{median_val}`"
        else:
            idx1, idx2 = (n // 2) - 1, n // 2
            v1, v2 = arr_sorted[idx1], arr_sorted[idx2]
            median_val = (v1 + v2) / 2
            phep_tinh_median = f"Số phần tử là **chẵn** ($N = {n}$), lấy trung bình cộng 2 vị trí giữa $\\frac{{{v1} + {v2}}}{{2}} = {median_val}$"
        st.write(
            f"🎯 **Median:** `{median_val}`"
            f"<br>&nbsp;&nbsp;&nbsp;&nbsp;👉 *Phép tính:* {phep_tinh_median}",
            unsafe_allow_html=True,)
        dem_tan_suat = {}
        for x in arr:
            dem_tan_suat[x] = dem_tan_suat.get(x, 0) + 1
        max_count = max(dem_tan_suat.values())
        modes = [val for val, count in dem_tan_suat.items() if count == max_count]
        mode_str = modes[0] if len(modes) == 1 else modes
        st.write(
            f"🔁 **Mode:** `{mode_str}`"
            f"<br>&nbsp;&nbsp;&nbsp;&nbsp;👉 *Phép tính:* Đếm số lần xuất hiện của các giá trị, giá trị xuất hiện nhiều nhất là **{max_count} lần**",
            unsafe_allow_html=True,)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    col1_ui, col2_ui = st.columns(2)
    tinh_va_hien_thi_chi_tiet(df.iloc[:, 1], col1_ui)
    tinh_va_hien_thi_chi_tiet(df.iloc[:, 2], col2_ui)
else:
    st.info("👈 Bạn hãy nhấn nút tải file `data5.8.csv` ở trên để xem kết quả!")