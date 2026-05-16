import streamlit as st
st.set_page_config(layout="wide", page_title="Dự án Nghệ sĩ yêu thích")
st.markdown("""
    <style>
    /* Ép ảnh trong các cột có chiều cao cố định và cắt phần thừa (object-fit) */
    [data-testid="stHorizontalBlock"] img {
        object-fit: cover;
        height: 280px; /* Bạn có thể tăng/giảm con số này để chỉnh độ dài ảnh */
        width: 100%;
        border-radius: 12px; /* Bo góc ảnh cho chuyên nghiệp */
    }
    </style>
    """, unsafe_allow_html=True)
artists = [
    {
        "id": "mj",
        "name": "Michael Jackson", 
        "full_name": "Michael Joseph Jackson",
        "img": "https://upload.wikimedia.org/wikipedia/commons/3/31/Michael_Jackson_in_1988.jpg", 
        "audio": "https://pub-c5e31b5cdafb419a86459dbe34ec61ee.r2.dev/Michael%20Jackson%20-%20Smooth%20Criminal.mp3", 
        "video": "https://www.youtube.com/watch?v=sOnqjkJTMaA",
        "bio": "Ông hoàng nhạc Pop với những bước nhảy Moonwalk và album Thriller kinh điển.",
        "more_imgs": [
            "https://cdn-p.smehost.net/sites/28d35d54a3c64e2b851790a18a1c4c18/wp-content/uploads/2021/07/210705_mj_perform_FEAT2.jpg",
            "https://i.pinimg.com/originals/9c/ef/8a/9cef8a0fa99a3ec9cf6fd481cec649a1.jpg"
        ],
        "img_titles": ["Thời kỳ Victory", "Kỷ nguyên Bad"]
    },
    {
        "id": "marino",
        "name": "Marino", 
        "full_name": "Marino Music",
        "img": "https://yt3.googleusercontent.com/U1Q4AbLiOQEChqq-0BltQUxh8fTQ5oEMkIyTXejSDRrffbH519fokn5s9_dSoTsQTAoTXP41bg=s160-c-k-c0x00ffffff-no-rj", 
        "audio": "https://pub-c5e31b5cdafb419a86459dbe34ec61ee.r2.dev/MARINO%20-%20Devil%20In%20Disguise.mp3", 
        "video": "https://www.youtube.com/watch?v=Af9nqVCKb-o",
        "bio": "Nghệ sĩ độc lập chuyên sản xuất những giai điệu lofi-hiphop, indie nhẹ nhàng.",
        "more_imgs": [
            "https://tse3.mm.bing.net/th/id/OIP.74Fk-FQwSq8CgAJAAIVwCQAAAA?pid=Api&h=220&P=0",
            "https://i.ytimg.com/vi/PrSjlpWu0cw/maxresdefault.jpg"
        ],
        "img_titles": ["Artwork Lust", "Thumbnail MV"]
    },
    {
        "id": "ngot",
        "name": "Ngọt", 
        "full_name": "Ngọt Band",
        "img": "https://doanhnhanonline.com.vn/wp-content/uploads/2025/02/Thang_Ngot.webp", 
        "audio": "https://pub-c5e31b5cdafb419a86459dbe34ec61ee.r2.dev/Ngot%20-%20Mat%20Tich.mp3", 
        "video": "https://www.youtube.com/watch?v=ECZVU4x6Xq0",
        "bio": "Một ban nhạc indie pop-rock xuất sắc bước ra từ Hà Nội với những giai điệu mộc mạc.",
        "more_imgs": [
            "https://kenh14cdn.com/203336854389633024/2024/4/30/edit-4382238819981418185472505072635779280973664n-17144857110642072113743.jpeg",
            "https://hrcwelive.com/wp-content/uploads/2022/12/thang-4-1024x679.jpg"
        ],
        "img_titles": ["Buổi họp báo", "Sân khấu chia tay"]
    },
    {
        "id": "bwu",
        "name": "BoyWithUke", 
        "full_name": "Charley Yang",
        "img": "https://yt3.ggpht.com/lVvSMrEbBFPHLBjMtXAMJCJuYGei45RrCpqAJepAxqOPp0UXMADSNlZhyA7WBNQgVYPqZI9m5w=s88-c-k-c0x00ffffff-no-rj", 
        "audio": "https://pub-c5e31b5cdafb419a86459dbe34ec61ee.r2.dev/BoyWithUke%20-%20Prairies.mp3", 
        "video": "https://www.youtube.com/watch?v=tIxLU8WUK1Y",
        "bio": "Nổi lên từ nền tảng TikTok với chiếc mặt nạ LED ẩn danh và cây đàn Ukulele.",
        "more_imgs": [
            "https://tse1.mm.bing.net/th/id/OIP.N8P_vEmZK81wE1soJH3HwAHaFj?pid=Api&h=220&P=0",
            "https://tse4.mm.bing.net/th/id/OIP.w5Bz1FNHNm6Cl--KFsrVzQHaEK?pid=Api&h=220&P=0"
        ],
        "img_titles": ["Mặt nạ LED", "Show face"]
    },
    {
        "id": "cg5",
        "name": "CG5", 
        "full_name": "Charlie Green",
        "img": "https://yt3.googleusercontent.com/8HpjM9EXS-wZ8t5No4MrNe5r6E9wb_JCblwkhFiyHatlnnxZKIKz_dNPY78iLC0XWU534NE0=s160-c-k-c0x00ffffff-no-rj", 
        "audio": "https://pub-c5e31b5cdafb419a86459dbe34ec61ee.r2.dev/CG5%20-%20Only%20In%20Ohio.mp3",
        "video": "https://www.youtube.com/watch?v=dxFYu-b8lv8&list=OLAK5uy_mYNnoC36fsA3BalOq5sQ1q4i0jZU2JP6M",
        "bio": "Ca sĩ, nhạc sĩ và nhà sản xuất âm nhạc người Mỹ nổi tiếng với các bài hát lấy cảm hứng từ game.",
        "more_imgs": [
            "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/09/cg5-with-guitar-cropped.jpg",
            "https://i.ytimg.com/vi/0URpHTfWB1Y/maxresdefault.jpg"
        ],
        "img_titles": ["Biểu diễn Live", "Banner âm nhạc"]
    }
]
if "selected_artist" not in st.session_state:
    st.session_state.selected_artist = artists[0]
current = st.session_state.selected_artist
with st.sidebar:
    st.title("Trắc nghiệm tính cách")
    st.write(f"Bạn chọn: {current['name']}")
    st.markdown("---")
    st.image(current["img"], use_container_width=True, caption=current["name"])
    st.markdown(f"**Họ và tên:** {current['full_name']}")
    st.markdown(f"**Nghệ danh:** {current['name']}")
    st.markdown(f"**Tiểu sử:**\n{current['bio']}")
st.title("Hãy chọn một nghệ sĩ bạn yêu thích")
cols = st.columns(len(artists))
for i, artist in enumerate(artists):
    with cols[i]:
        if st.button(artist["name"], key=f"btn_{artist['id']}", use_container_width=True):
            st.session_state.selected_artist = artist
            st.rerun()
with st.expander(current["name"], expanded=True):
    st.subheader("Bài hát yêu thích")
    st.audio(current["audio"])
    st.subheader("MV yêu thích")
    st.video(current["video"])
    st.divider()
    st.subheader("Một số hình ảnh khác")
    st.caption("Hình ảnh và khoảnh khắc ấn tượng")
    num_imgs = len(current["more_imgs"])
    if num_imgs > 0:
        img_cols = st.columns(num_imgs)
        for idx in range(num_imgs):
            with img_cols[idx]:
                st.image(
                    current["more_imgs"][idx], 
                    use_container_width=True,
                    caption=current["img_titles"][idx]
                )