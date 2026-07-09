#python -m streamlit run main15.py
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Đặt tiêu đề cho ứng dụng
st.title("Phổ Điểm Thi Tuyển Sinh Lớp 10 Thành Phố Phan Thiết")
st.subheader("Thực hành vẽ biểu đồ cột biểu diễn phổ điểm 3 môn: Toán, Ngữ Văn, Tiếng Anh")

# 1. Tạo bộ dữ liệu giả lập mẫu cho phổ điểm thi lớp 10
# Các khoảng điểm từ 0-2, 2-4, 4-6, 6-8, và 8-10 điểm
data = [
    {"Khoảng điểm": "0 - 2", "Môn học": "Toán", "Số lượng học sinh": 150},
    {"Khoảng điểm": "0 - 2", "Môn học": "Ngữ Văn", "Số lượng học sinh": 45},
    {"Khoảng điểm": "0 - 2", "Môn học": "Tiếng Anh", "Số lượng học sinh": 120},
    
    {"Khoảng điểm": "2 - 4", "Môn học": "Toán", "Số lượng học sinh": 380},
    {"Khoảng điểm": "2 - 4", "Môn học": "Ngữ Văn", "Số lượng học sinh": 210},
    {"Khoảng điểm": "2 - 4", "Môn học": "Tiếng Anh", "Số lượng học sinh": 460},
    
    {"Khoảng điểm": "4 - 6", "Môn học": "Toán", "Số lượng học sinh": 850},
    {"Khoảng điểm": "4 - 6", "Môn học": "Ngữ Văn", "Số lượng học sinh": 1150},
    {"Khoảng điểm": "4 - 6", "Môn học": "Tiếng Anh", "Số lượng học sinh": 720},
    
    {"Khoảng điểm": "6 - 8", "Môn học": "Toán", "Số lượng học sinh": 920},
    {"Khoảng điểm": "6 - 8", "Môn học": "Ngữ Văn", "Số lượng học sinh": 980},
    {"Khoảng điểm": "6 - 8", "Môn học": "Tiếng Anh", "Số lượng học sinh": 810},
    
    {"Khoảng điểm": "8 - 10", "Môn học": "Toán", "Số lượng học sinh": 410},
    {"Khoảng điểm": "8 - 10", "Môn học": "Ngữ Văn", "Số lượng học sinh": 320},
    {"Khoảng điểm": "8 - 10", "Môn học": "Tiếng Anh", "Số lượng học sinh": 590},
]

df = pd.DataFrame(data)

# Hiển thị bảng dữ liệu mẫu bên dưới
with st.expander("Xem bảng dữ liệu chi tiết"):
    st.dataframe(df)

# 2. Cấu hình biểu đồ cột nhóm bằng Vega-Lite
vega_lite_spec = {
    "mark": {"type": "bar", "tooltip": True},
    "encoding": {
        # Trục X đại diện cho các khoảng điểm thi
        "x": {
            "field": "Khoảng điểm",
            "type": "nominal",
            "axis": {"title": "Khoảng điểm thi (Điểm)"}
        },
        # Trục Y đại diện cho số lượng thí sinh đạt được khoảng điểm đó
        "y": {
            "field": "Số lượng học sinh",
            "type": "quantitative",
            "axis": {"title": "Số lượng học sinh (Thí sinh)"}
        },
        # xOffset giúp tách các cột môn học đứng cạnh nhau trong cùng 1 khoảng điểm
        "xOffset": {
            "field": "Môn học"
        },
        # Tự động phân chia màu sắc dựa trên tên môn học
        "color": {
            "field": "Môn học",
            "type": "nominal",
            "scale": {
                "domain": ["Toán", "Ngữ Văn", "Tiếng Anh"],
                "range": ["#e74c3c", "#f39c12", "#3498db"]  # Màu Đỏ (Toán), Vàng (Văn), Xanh dương (Anh)
            },
            "legend": {"title": "Danh sách môn thi"}
        }
    },
    "config": {
        "bar": {"cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4} # Bo góc nhẹ đỉnh cột cho đẹp mắt
    }
}

# 3. Gọi hàm vẽ biểu đồ lên ứng dụng Streamlit
st.vega_lite_chart(df, vega_lite_spec, use_container_width=True)

