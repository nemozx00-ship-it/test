#python -m streamlit run main15.py
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

st.title("Phổ Điểm Thi Tuyển Sinh Lớp 10")
st.subheader("phổ điểm chi tiết (0 - 10) cho 3 môn học")

# 1. Khởi tạo dữ liệu giả lập chi tiết từ 0 đến 10 điểm cho cả 3 môn
# Mỗi mức điểm (0, 1, 2, ..., 10) sẽ có số lượng học sinh riêng biệt
points = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data_toan = [{"Điểm": p, "Môn": "Toán", "Số lượng học sinh": v} for p, v in zip(points, [20, 50, 110, 230, 310, 540, 610, 420, 310, 180, 50])]
data_van = [{"Điểm": p, "Môn": "Ngữ Văn", "Số lượng học sinh": v} for p, v in zip(points, [5, 15, 35, 80, 170, 420, 680, 520, 310, 110, 15])]
data_anh = [{"Điểm": p, "Môn": "Tiếng Anh", "Số lượng học sinh": v} for p, v in zip(points, [30, 65, 140, 210, 320, 480, 410, 360, 310, 220, 90])]

# Gộp chung vào một DataFrame để dễ quản lý dữ liệu
df_toan = pd.DataFrame(data_toan)
df_van = pd.DataFrame(data_van)
df_anh = pd.DataFrame(data_anh)

# Hàm tạo cấu hình biểu đồ cột đơn lẻ cho từng môn bằng Vega-Lite
def create_vega_spec(mon_hoc, mau_sac):
    return {
        "mark": {"type": "bar", "tooltip": True},
        "encoding": {
            "x": {
                "field": "Điểm",
                "type": "ordinal",  # Định dạng dạng thứ tự để hiển thị rõ từ cột số 0 đến cột số 10
                "axis": {"title": "Mức điểm chi tiết"}
            },
            "y": {
                "field": "Số lượng học sinh",
                "type": "quantitative",
                "axis": {"title": "Số lượng học sinh (Thí sinh)"}
            },
            "color": {
                "value": mau_sac  # Giữ nguyên màu đặc trưng của từng môn như biểu đồ cũ
            }
        },
        "config": {
            "bar": {"cornerRadiusTopLeft": 3, "cornerRadiusTopRight": 3}
        }
    }

# 2. Sử dụng cấu trúc tab của Streamlit để hiển thị riêng biệt 3 môn 3 biểu đồ
tab1, tab2, tab3 = st.tabs(["Môn Toán", "Môn Ngữ Văn", "Môn Tiếng Anh"])

with tab1:
    st.write("### Phổ điểm chi tiết môn Toán")
    spec_toan = create_vega_spec("Toán", "#e74c3c")  # Màu đỏ
    st.vega_lite_chart(df_toan, spec_toan, use_container_width=True)

with tab2:
    st.write("### Phổ điểm chi tiết môn Ngữ Văn")
    spec_van = create_vega_spec("Ngữ Văn", "#f39c12")  # Màu vàng/cam
    st.vega_lite_chart(df_van, spec_van, use_container_width=True)

with tab3:
    st.write("### Phổ điểm chi tiết môn Tiếng Anh")
    spec_anh = create_vega_spec("Tiếng Anh", "#3498db")  # Màu xanh dương
    st.vega_lite_chart(df_anh, spec_anh, use_container_width=True)