import streamlit as st
import random

# --- Cấu hình trang ---
st.set_page_config(page_title="FNAF Pizzeria Tycoon", page_icon="🐻", layout="wide")

# --- Khởi tạo dữ liệu Game (Session State) ---
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.money = 1000  
    st.session_state.day = 1
    st.session_state.max_days = 5  
    st.session_state.target_money = 5000  
    st.session_state.reviews = ["Nhà hàng mới mở, trông hơi trống trải."]
    st.session_state.game_over = False
    st.session_state.game_won = False
    
    st.session_state.inventory = {
        "animatronics": {"Freddy Fazbear": 0, "Bonnie": 0, "Chica": 0, "Foxy": 0},
        "decorations": {"Bóng bay & Ruy băng": 0, "Bàn tiệc VIP": 0, "Đèn neon sàn diễn": 0},
        # Đã thêm hố bóng vào danh sách sở hữu ban đầu
        "arcade": {"Máy gắp thú": 0, "Máy điện tử thùng 8-bit": 0, "Hố bóng sắc màu": 0}
    }

# --- DỮ LIỆU CỬA HÀNG (ĐÃ THÊM HỐ BÓNG) ---
ITEMS_DATA = {
    "animatronics": {
        "Freddy Fazbear": {
            "price": 800, "bonus": 300, 
            "desc": "Gấu máy chính. Thu hút cực đông khách trẻ em.", 
            "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1825be98-aa8b-4ba1-be17-c4580af90127/ddvpacn-aaf6abb6-abc8-4c54-863e-923f3c95d871.png/v1/fill/w_670,h_1192/fnaf_help_wanted_freddy_by_r_jamesrenders_ddvpacn-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzI2NCIsInBhdGgiOiJcL2ZcLzE4MjViZTk4LWFhOGItNGJhMS1iZTE3LWM0NTgwYWY5MDEyN1wvZGR2cGFjbi1hYWY2YWJiNi1hYmM4LTRjNTQtODYzZS05MjNmM2M5NWQ4NzEucG5nIiwid2lkdGgiOiI8PTE4MzYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.QSL0Ws8Hej7OxMtdCN2Wcijqp1sDWs9Gi3nIXu16l-I"
        },
        "Bonnie": {
            "price": 500, "bonus": 150, 
            "desc": "Chú thỏ đánh guitar. Tăng độ phấn khích.", 
            "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6d313138-65c7-4b7d-9d13-14195affde2d/defhvha-4032c770-9074-4d04-84da-6e7a826125d3.png/v1/fill/w_785,h_1018/fnaf_vr_help_wanted_bonnie_by_optimushunter29_defhvha-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI5NiIsInBhdGgiOiJcL2ZcLzZkMzEzMTM4LTY1YzctNGI3ZC05ZDEzLTE0MTk1YWZmZGUyZFwvZGVmaHZoYS00MDMyYzc3MC05MDc0LTRkMDQtODRkYS02ZTdhODI2MTI1ZDMucG5nIiwid2lkdGgiOiI8PTEwMDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.KK3rUs8o4oy_PPJTVv2y_9XFK_4rQRTQS9cwXupjLFk"
        },
        "Chica": {
            "price": 500, "bonus": 150, 
            "desc": "Gà Chica mang bánh cupcake. Giúp khách ăn nhiều hơn.", 
            "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6d313138-65c7-4b7d-9d13-14195affde2d/defhvlg-46b5598c-0707-4975-bac1-a03edd801d88.png/v1/fill/w_740,h_1080/fnaf_vr_help_wanted_chica_by_optimushunter29_defhvlg-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ1OSIsInBhdGgiOiJcL2ZcLzZkMzEzMTM4LTY1YzctNGI3ZC05ZDEzLTE0MTk1YWZmZGUyZFwvZGVmaHZsZy00NmI1NTk4Yy0wNzA3LTQ5NzUtYmFjMS1hMDNlZGQ4MDFkODgucG5nIiwid2lkdGgiOiI8PTEwMDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.JCtMtklAuGo_NdZdmwiHmpMsoDSIDYhLjrOTLjB6ox8"
        },
        "Foxy": {
            "price": 700, "bonus": 250, 
            "desc": "Cáo cướp biển vùng Pirate Cove. Khách cực kỳ thích.", 
            "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/599743c7-9070-437a-bf99-ab244f60455b/df72y69-92e1f908-52bb-4206-ad2f-4caf1656bfbe.png/v1/fill/w_726,h_1100/_fnaf_hw_sfm__captain_foxy_by_zoinkeesuwu_df72y69-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkzOSIsInBhdGgiOiJcL2ZcLzU5OTc0M2M3LTkwNzAtNDM3YS1iZjk5LWFiMjQ0ZjYwNDU1YlwvZGY3Mnk2OS05MmUxZjkwOC01MmJiLTQyMDYtYWQyZi00Y2FmMTY1NmJmYmUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.-nVU5kNkEZ86NgPwV_Aa4N1V6LclOJLwQKF5qEeAjpo"
        },
    },
    "decorations": {
        "Bóng bay & Ruy băng": {
            "price": 150, "bonus": 40, 
            "desc": "Trang trí cơ bản giúp giảm bớt vẻ âm u.", 
            "img": "https://vignette.wikia.nocookie.net/freddy-fazbears-pizza/images/4/4c/Balloon_Barrel_-_Cat%C3%A1logo_%28FFPS%29.png/revision/latest?cb=20180221055605&path-prefix=es"
        },
        "Bàn tiệc VIP": {
            "price": 400, "bonus": 120, 
            "desc": "Bàn dài cho các bữa tiệc sinh nhật tốn kém.", 
            "img": "https://i.pinimg.com/originals/54/99/5f/54995fa762172b0f947f124ec0dbf46a.jpg"
        },
        "Đèn neon sàn diễn": {
            "price": 350, "bonus": 100, 
            "desc": "Làm nổi bật các animatronic trên sân khấu.", 
            "img": "https://cf.shopee.vn/file/a4d0481de41acf443d2f22e21c65c19f"
        },
    },
    "arcade": {
        "Máy gắp thú": {
            "price": 300, "bonus": 80, 
            "desc": "Trò chơi may rủi, trẻ em rất thích nạp tiền.", 
            "img": "https://i.pinimg.com/originals/be/c4/6f/bec46fdccca294cef98a766e5e6cc563.jpg"
        },
        "Máy điện tử thùng 8-bit": {
            "price": 600, "bonus": 200, 
            "desc": "Máy chơi game cổ điển sinh lời cao.", 
            "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/60e3b4f6-a250-4f39-b40a-7c4d5e8e8c75/di0v1ih-d8a9f845-5ad0-47a0-89d1-23cfc2094c3e.png/v1/fill/w_894,h_894,q_70,strp/fnaf_arcade_by_amandexh_di0v1ih-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjA0OCIsInBhdGgiOiJcL2ZcLzYwZTNiNGY2LWEyNTAtNGYzOS1iNDBhLTdjNGQ1ZThlOGM3NVwvZGkwdjFpaC1kOGE5Zjg0NS01YWQwLTQ3YTAtODlkMS0yM2NmYzIwOTRjM2UucG5nIiwid2lkdGgiOiI8PTIwNDgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.eJcRjhEg-C9JcOBEBvItT0FzUfaj3KPvr_dJgZ1v3eQ"
        },
        # THÔNG TIN VẬT PHẨM MỚI: HỐ BÓNG
        "Hố bóng sắc màu": {
            "price": 450, "bonus": 160, 
            "desc": "Khu vực hố bóng cho trẻ em nghịch ngợm. Hãy cẩn thận kẻo có thứ gì trốn bên dưới...", 
            "img": "https://tse1.mm.bing.net/th/id/OIP.oxnTh8Y_vnEJ5r9xWe1jFQHaEX?pid=Api&h=220&P=0"
        },
    }
}

# Ngân hàng lời phê của khách
GOOD_REVIEWS = [
    "Đồ ăn ngon, các chú robot biểu diễn rất dễ thương!",
    "Mấy con animatronic đỉnh quá, con tôi cứ đòi xem mãi.",
    "Không gian cửa hàng rất tuyệt, máy chơi game chơi rất cuốn.",
    "Mấy đứa nhỏ mê tít cái hố bóng mới lắp!",
    "Một nơi tuyệt vời để tổ chức sinh nhật!"
]

BAD_REVIEWS = [
    "Nhà hàng gì mà tối tăm, đáng sợ quá...",
    "Tôi thề là đã thấy con robot tự di chuyển trong góc tối!",
    "Chẳng có gì giải trí cả, chán ngắt.",
    "Hình như có ai đó hoặc thứ gì đó đang nhìn tôi từ dưới hố bóng...",
    "Không khí ở đây cứ có mùi gì đó kỳ lạ..."
]

def get_total_bonus():
    bonus_money = 0
    total_items = 0
    for category in st.session_state.inventory:
        for item, count in st.session_state.inventory[category].items():
            bonus_money += count * ITEMS_DATA[category][item]["bonus"]
            total_items += count
    return bonus_money, total_items

def run_business():
    if st.session_state.game_over or st.session_state.game_won:
        return

    bonus, total_items = get_total_bonus()
    base_income = random.randint(200, 600)
    total_income = base_income + bonus
    st.session_state.money += total_income
    
    good_review_chance = min(30 + (total_items * 15), 90) 
    
    if random.randint(1, 100) <= good_review_chance:
        review = random.choice(GOOD_REVIEWS) + f" (+{total_income} VNĐ)"
    else:
        review = random.choice(BAD_REVIEWS) + f" (+{total_income} VNĐ)"
        
    st.session_state.reviews.insert(0, f"Ngày {st.session_state.day}: {review}")
    
    if st.session_state.day < st.session_state.max_days:
        st.session_state.day += 1
    else:
        if st.session_state.money >= st.session_state.target_money:
            st.session_state.game_won = True
        else:
            st.session_state.game_over = True

def reset_game():
    del st.session_state.initialized
    st.rerun()

# =================================================================
# --- GIAO DIỆN CHÍNH ---
# =================================================================

st.title("🐻 Menu Freddy Fazbear's Pizzeria")
st.write("Vui lòng chọn số lượng cho vật dụng giải trí, trang trí và bấm nút **Kinh Doanh**.")

with st.sidebar:
    st.header("📊 BẢNG ĐIỀU KHIỂN")
    st.metric(label="📆 Ngày hiện tại", value=f"{st.session_state.day} / {st.session_state.max_days}")
    st.metric(label="💰 Tiền hiện có", value=f"{st.session_state.money:,} VNĐ")
    st.metric(label="🎯 Chỉ tiêu Ngày 5", value=f"{st.session_state.target_money:,} VNĐ")
    
    bonus_money, _ = get_total_bonus()
    st.caption(f"📈 Bonus thu nhập mỗi ngày: +{bonus_money:,} VNĐ")
    
    st.write("---")
    st.subheader("💬 Đánh giá từ Khách hàng:")
    for rev in st.session_state.reviews[:6]:
        if "🥇" in rev or "+" in rev and not any(bad in rev for bad in ["tối tăm", "di chuyển", "chán", "mùi", "nhìn tôi"]):
            st.success(rev)
        else:
            st.error(rev)
            
    if st.button("🔄 Chơi lại từ đầu", use_container_width=True):
        reset_game()

if st.session_state.game_won:
    st.balloons()
    st.success(f"🎉 CHÚC MỪNG! Bạn đã sống sót qua 5 đêm và đạt doanh thu {st.session_state.money:,} VNĐ!")
elif st.session_state.game_over:
    st.error(f"💀 GAME OVER! Bạn không đạt đủ chỉ tiêu {st.session_state.target_money:,} VNĐ.")
else:
    tab_business, tab_animatronic, tab_decor, tab_arcade = st.tabs([
        "💼 Kinh Doanh", 
        "🤖 Animatronics", 
        "🎈 Đồ Trang Trí", 
        "🕹️ Máy Giải Trí (Arcade)"
    ])

    with tab_business:
        st.subheader("Hôm nay bạn muốn mở cửa nhà hàng chứ?")
        if st.button("🔔 BẮT ĐẦU KINH DOANH HÔM NAY", type="primary", use_container_width=True):
            run_business()
            st.rerun()

    def render_shop_tab(category_key):
        items = ITEMS_DATA[category_key]
        for item_name, info in items.items():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(info['img'], use_container_width=True)
            
            with col2:
                st.subheader(item_name)
                st.write(f"**Giá:** <span style='color:green;'>{info['price']:,} VNĐ</span>", unsafe_allow_html=True)
                st.write(f"**Hiệu ứng:** +{info['bonus']} VNĐ thu nhập/ngày")
                st.caption(info['desc'])
                
                current_qty = st.session_state.inventory[category_key][item_name]
                
                new_qty = st.number_input(
                    label=f"Số lượng {item_name}",
                    min_value=0,
                    max_value=10,
                    value=current_qty,
                    step=1,
                    key=f"input_{category_key}_{item_name}"
                )
                
                if new_qty != current_qty:
                    diff = new_qty - current_qty
                    cost = diff * info['price']
                    
                    if diff > 0 and st.session_state.money < cost:
                        st.error("Bạn không đủ tiền để mua thêm số lượng vật phẩm này!")
                    else:
                        st.session_state.money -= cost
                        st.session_state.inventory[category_key][item_name] = new_qty
                        st.rerun()
                        
            st.write("---")

    with tab_animatronic:
        render_shop_tab("animatronics")

    with tab_decor:
        render_shop_tab("decorations")

    with tab_arcade:
        render_shop_tab("arcade")
#python -m streamlit run main12.py