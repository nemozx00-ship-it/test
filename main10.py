#python -m streamlit run main10.py
import streamlit as st

st.set_page_config(
    page_title="Nhà Hàng Lê Lợi", 
    page_icon="🍱",
    layout="centered"
)
menu_data = {
    'Khai Vị': {
        'Khoai tây chiên': {'price': 25000, 'img': 'https://cdn-www.vinid.net/7993a7a3-cach-lam-khoai-tay-chien-1.jpg'},
        'Salad trộn': {'price': 35000, 'img': 'https://phunugioi.com/wp-content/uploads/2020/11/cach-lam-salad-tron.jpg'}
    },
    'Món Chính': {
        'Mì Ý sốt bò bằm': {'price': 55000, 'img': 'https://cookbeo.com/media/2021/10/mi-y/thumbnails/mi-y-4x3-1200.jpg'},
        'Cá viên + Bò viên + Hot dog': {'price': 40000, 'img': 'https://www.cet.edu.vn/wp-content/uploads/2018/04/ca-vien-chien.jpg'},
        'Gà rán': {'price': 45000, 'img': 'https://img5.thuthuatphanmem.vn/uploads/2021/12/14/hinh-anh-ga-ran-chien-gion_024410978.jpg'},
        'Cánh gà chiên mắm': {'price': 50000, 'img': 'https://i.ytimg.com/vi/ozNNdCjKQzM/maxresdefault.jpg'},
        'Sườn non nấu đậu + Bánh mì': {'price': 65000, 'img': 'https://amthucdochay.com/wp-content/uploads/2021/08/bo-lagu-2.jpg'}
    },
    'Tráng Miệng': {
        'Chè đậu xanh': {'price': 15000, 'img': 'https://i.ytimg.com/vi/SjFnBMeBxQ/maxresdefault.jpg'},
        'Trái cây tươi': {'price': 20000, 'img': 'https://cdn-www.vinid.net/2020/05/b5305080-20200428_appvinid_bannerweb_cattuong_1.jpg'}
    }
}
st.image("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=2070&auto=format&fit=crop", 
         caption="Chào mừng đến với Nhà Hàng Ông VKhang",
         use_container_width=True)
st.title("🏯 Menu nhà hàng Ông Vkhang")
st.write("Vui lòng chọn số lượng cho các món ăn yêu thích và nhấn Submit để tính tiền.")
with st.form(key='order_form'):
    tabs = st.tabs(["🍟 Khai Vị", "🍝 Món Chính", "🍰 Tráng Miệng"])
    order_quantities = {}
    for i, category in enumerate(menu_data.keys()):
        with tabs[i]:
            for item, info in menu_data[category].items():
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(info['img'], use_container_width=True)
                with col2:
                    st.subheader(item)
                    st.write(f"Giá: **{info['price']:,} VNĐ**")
                    order_quantities[item] = st.number_input(f"Số lượng {item}", min_value=0, step=1, key=f"qty_{item}")
                st.write("---")
    submitted = st.form_submit_button('XÁC NHẬN & TÍNH TIỀN')
if submitted:
    st.header("🧾 Hóa đơn của bạn")
    total_bill = 0
    has_item = False
    all_food = {**menu_data['Khai Vị'], **menu_data['Món Chính'], **menu_data['Tráng Miệng']}
    for item, qty in order_quantities.items():
        if qty > 0:
            has_item = True
            price = all_food[item]['price']
            subtotal = qty * price
            total_bill += subtotal
            st.write(f"- **{item}**: {qty} phần x {price:,} = **{subtotal:,} VNĐ**")
    if not has_item:
        st.warning("Bạn chưa chọn món nào cả!")
    else:
        st.divider()
        st.subheader(f"TỔNG CỘNG: :red[{total_bill:,} VNĐ]")
        st.balloons()