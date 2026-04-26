import streamlit as st
st.set_page_config(page_title="Login Page")
st.markdown("LOGIN")
username = st.text_input("Username:")
password = st.text_input("Password:", type="password")
if st.button("LOGIN"):
    if username == "admin" and password == "12345":
        st.success("Đăng nhập thành công!")
    else:
        st.error("Sai tên đăng nhập hoặc mật khẩu!")