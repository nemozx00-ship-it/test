# python -m streamlit run main22.py
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
def login_screen():
    st.title("E-BIKE")
    with st.form("login_form"):
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")
        submit = st.form_submit_button("Đăng nhập", type="primary")
        if submit:
            if username == "admin" and password == "123":
                st.session_state.logged_in = True
                st.success("Đăng nhập thành công!")
                st.rerun()
            else:
                st.error("Tên đăng nhập hoặc mật khẩu không đúng!")
def bike_rental_screen():
    col_title, col_logout = st.columns([4, 1])
    with col_title:
        st.title("E-BIKE - Dịch Vụ Thuê Xe")
    with col_logout:
        st.write("")
        if st.button("Đăng xuất"):
            st.session_state.logged_in = False
            st.rerun()
    current_file_dir = Path(__file__).resolve().parent
    possible_folders = [
        current_file_dir / "E-bike",
        current_file_dir / "hkd" / "E-bike",
    ]
    images = []
    for folder in possible_folders:
        if folder.exists():
            for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
                images.extend(list(folder.glob(ext)))
            if images:
                break
    if not images:
        images = [
            "C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\E-bike\\img1.jpg",
            "C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\E-bike\\img2.jpg",
            "C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\E-bike\\img3.png",
            "C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\E-bike\\img4.jpg",
            "C:\\Users\\Nhat Kieu\\Desktop\\New folder\\hkd\\E-bike\\img5.jpg",
        ]
    NUM_COLS = 4
    num_rows = (len(images) + NUM_COLS - 1) // NUM_COLS
    for row_idx in range(num_rows):
        cols = st.columns(NUM_COLS)
        for col_idx in range(NUM_COLS):
            img_idx = row_idx * NUM_COLS + col_idx
            if img_idx < len(images):
                with cols[col_idx]:
                    img_item = images[img_idx]
                    img_src = str(img_item) if isinstance(img_item, Path) else img_item          
                    st.image(img_src, use_container_width=True)
                    st.write("XL: ...")
                    st.write("Giá: ...")
    st.divider()
    if st.button("Thuê xe", type="primary"):
        st.success("Đã bấm Thuê xe!")
if not st.session_state.logged_in:
    login_screen()
else:
    bike_rental_screen()