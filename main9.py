import streamlit as st

# 1. Cấu hình trang web
st.set_page_config(
    page_title='FNAF Ultimate Entity Database', 
    page_icon=':robot:', 
    layout='wide'
)

# 2. Cơ sở dữ liệu khổng lồ (Cộng dồn và bổ sung mới)
fnaf_data = {
        'FNAF 1': {
        'title': "Five Nights at Freddy's 1 (8/8/2014)",
        'protagonist': 'Mike Schmidt',
        'content': 'Bối cảnh diễn ra tại nhà hàng Freddy Fazbear s Pizza cũ kỹ. Người chơi vào vai Mike Schmidt, làm việc ca đêm từ 12h sáng đến 6h sáng với mức lương ít ỏi, trong khi phải đối mặt với các linh hồn ám vào thú máy đang tìm cách trả thù.',
        'gameplay': 'Đóng cửa, bật đèn và quản lý điện năng, sinh tồn đến 6 giờ sáng khỏi 5 Animatronics.',
        'all_animatronics': 'Freddy, Bonnie, Chica, Foxy, Golden Freddy, Endoskeleton (Endo-01).',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/319510/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=RP4UTOek0-Y',
        'jumpscare_audio': 'https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptoken=87f176b9-92f7-4636-8e8e-8a032d84719e',
        'gallery': [
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e74ba232-4a66-4cab-8128-fd1b2fe807dc/dja1kwh-c47f5b20-f5d6-4da2-8877-e43abf14fbe9.png/v1/fill/w_826,h_968/_fnaf_1__freddy_fazbear_render_by_iqiwiwiwi_dja1kwh-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2U3NGJhMjMyLTRhNjYtNGNhYi04MTI4LWZkMWIyZmU4MDdkY1wvZGphMWt3aC1jNDdmNWIyMC1mNWQ2LTRkYTItODg3Ny1lNDNhYmYxNGZiZTkucG5nIiwid2lkdGgiOiI8PTEwOTIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.1KDC5tVEXoNNeTcBay2Ldcjc6Lf4VM_7k97uWvj7CLU', 'name': 'Freddy'},
            {'url': 'https://i.pinimg.com/736x/66/d1/61/66d1610980d64517262894038d66ffe6.jpg', 'name': 'Bonnie'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/dd7d7xc-e1dad558-5df2-4d1a-8eab-2aefa251cc14.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGQ3ZDd4Yy1lMWRhZDU1OC01ZGYyLTRkMWEtOGVhYi0yYWVmYTI1MWNjMTQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.-v9WfUjuB6Vpfo5p4cNk8y1oKUwNmVYXA7vVbrNxaJg', 'name': 'Chica'},
            {'url': 'https://www.nicepng.com/png/detail/224-2242439_more-like-fnaf-1-foxy-the-pirate-fox.png', 'name': 'Foxy'},
            {'url': 'https://tse4.mm.bing.net/th/id/OIP.VZsjQoOmwzVvc_6gfPVnUQHaHa?pid=Api&h=220&P=0', 'name': 'Golden Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4d8bc58d-24ec-4d96-8688-f7f3cf37f330/dbc2vo0-d9ee6790-3ffd-4fd0-895e-9052bd7221a0.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzRkOGJjNThkLTI0ZWMtNGQ5Ni04Njg4LWY3ZjNjZjM3ZjMzMFwvZGJjMnZvMC1kOWVlNjc5MC0zZmZkLTRmZDAtODk1ZS05MDUyYmQ3MjIxYTAucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.n9YPVDswRpQBDlP2ZrrRkYRTrwd9eWmXz6TTYZmYWWE', 'name': 'Endoskeleton (Endo-01)'}
        ]
    },
    'FNAF 2': {
        'title': "Five Nights at Freddy's 2 (11/11/2014)",
        'protagonist': 'Jeremy Fitzgerald (Đêm 1-6) / Fritz Smith (Đêm 7)',
        'content': 'Diễn ra năm 1987. Nhà hàng mới với dàn thú máy hiện đại nhưng hệ thống nhận diện tội phạm bị hỏng.',
        'gameplay': 'Không có cửa sập. Bạn phải đeo Mặt nạ Freddy thật nhanh khi Animatronics vào phòng. Luôn phải lên dây cót hộp nhạc (Music Box) để ngăn chặn The Puppet. Sử dụng đèn pin để xua đuổi Foxy và sinh tồn đến 6 giờ sáng.',
        'all_animatronics': 'Scraps, Rockstars, Mediocre Melodies, Posh Pizza, Trash & Gang, Support Units.',
        'main_img': 'https://tse1.mm.bing.net/th/id/OIP.XBBI4T6-2Rst_UcDy7lJMQHaFE?pid=Api&h=220&P=0',
        'video': 'https://www.youtube.com/watch?v=lVPONdZBh6s',
        'jumpscare_audio': 'https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptoken=645a8637-2591-49b0-9426-5b430e386001',
        'gallery': [
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddf3j5v-d44a44bb-1e03-454e-b112-68a10217ed46.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGRmM2o1di1kNDRhNDRiYi0xZTAzLTQ1NGUtYjExMi02OGExMDIxN2VkNDYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.jX_nAyZZLseispJO4ZBfPor2Q0UsdNG1W2_BSRYM9BE', 'name': 'Toy Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c2a9ca4b-c488-4134-8217-ebc444ec74c0/dfp7mzm-9089fc7c-7544-4fe0-bff4-a14adab0ff36.png/v1/fill/w_760,h_1052/fnaf_2_toy_bonnie_c4d_render_by_puchaolxd_dfp7mzm-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc3MSIsInBhdGgiOiJcL2ZcL2MyYTljYTRiLWM0ODgtNDEzNC04MjE3LWViYzQ0NGVjNzRjMFwvZGZwN216bS05MDg5ZmM3Yy03NTQ0LTRmZTAtYmZmNC1hMTRhZGFiMGZmMzYucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.cgr4EvMWCC31dntJAYPh5aVI2B0W78SPh_kJ71PgG-w', 'name': 'Toy Bonnie'},
            {'url': 'https://tse3.mm.bing.net/th/id/OIP.utxPIoaNnKxhrScRRSLJVgHaJz?pid=Api&h=220&P=0', 'name': 'Toy Chica'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddqwpi7-ec0a5fdd-b6c1-44c9-b464-42a00b7ee28d.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGRxd3BpNy1lYzBhNWZkZC1iNmMxLTQ0YzktYjQ2NC00MmEwMGI3ZWUyOGQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.CB1Fsu3GaoAXlNiiFo_BWIjqe_fyvoHoShWC3hUJsVw', 'name': 'Mangle'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c2a9ca4b-c488-4134-8217-ebc444ec74c0/dfp8vr2-86ba20c8-b2fb-4ef7-812e-b5874c336dcf.png/v1/fill/w_1280,h_1916/fnaf_2_puppet_c4d_render_by_puchaolxd_dfp8vr2-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkxNiIsInBhdGgiOiJcL2ZcL2MyYTljYTRiLWM0ODgtNDEzNC04MjE3LWViYzQ0NGVjNzRjMFwvZGZwOHZyMi04NmJhMjBjOC1iMmZiLTRlZjctODEyZS1iNTg3NGMzMzZkY2YucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.CPlYvknRSyGcz9aztPcMWoOcYMpULz_Cr-UicXNbgAA', 'name': 'Puppet'},
            {'url': 'https://vignette.wikia.nocookie.net/freddy-fazbears-pizza/images/b/b6/FNAF2BB.png/revision/latest?cb=20141111111744', 'name': 'BB'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddejev3-12bc95e2-de58-446e-9c0e-3c92c028b48b.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGRlamV2My0xMmJjOTVlMi1kZTU4LTQ0NmUtOWMwZS0zYzkyYzAyOGI0OGIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.IIOYhcuBub6FfHOvXbwcigBsv_i-1mmyLkhqKJzwk3c', 'name': 'JJ'},
            {'url': 'https://i.pinimg.com/236x/45/d5/5e/45d55e2e8572f0cd31fb7c01c68c1b9b.jpg', 'name': 'Endoskeleton (Endo-02)'},
            {'url': 'https://www.nicepng.com/png/detail/158-1584120_withered-freddy-five-nights-at-freddys-withered-freddy.png', 'name': 'W. Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/20b9c2e7-816e-4946-ba00-85a35a72d02a/dflktof-18b3702b-ac13-4dc0-ac27-9b1140f44595.png/v1/fill/w_601,h_1330/withered_bonnie_full_body____fnaf_2__by_thesubjact_dflktof-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTk0NCIsInBhdGgiOiJcL2ZcLzIwYjljMmU3LTgxNmUtNDk0Ni1iYTAwLTg1YTM1YTcyZDAyYVwvZGZsa3RvZi0xOGIzNzAyYi1hYzEzLTRkYzAtYWMyNy05YjExNDBmNDQ1OTUucG5nIiwid2lkdGgiOiI8PTg3OSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.na8fEyxkGT4aljS9SMsYO382KFr21dpB5GIpzIgb3j4', 'name': 'W. Bonnie'},
            {'url': 'https://www.kindpng.com/picc/m/559-5595386_withered-chica-png-download-fnaf-2-withered-chica.png', 'name': 'W. Chica'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddp23k8-c1974cf9-64c6-4f0d-a5b8-c81fd983e8ea.png/v1/fill/w_624,h_1106,strp/fnaf_2_withered_foxy_full_body_by_enderziom2004_ddp23k8-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTEwNiIsInBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGRwMjNrOC1jMTk3NGNmOS02NGM2LTRmMGQtYTViOC1jODFmZDk4M2U4ZWEucG5nIiwid2lkdGgiOiI8PTYyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.s2dWWSRPtKvo0Xs0lHcrtHZ5LkJbFsFCPqdpmx53pqk', 'name': 'W. Foxy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/dd8xcd4-7a8a919c-706b-4415-8f55-e1bf319d14c3.png/v1/fill/w_636,h_607,strp/fnaf_2_withered_golden_freddy_full_body_by_enderziom2004_dd8xcd4-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjA3IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZDh4Y2Q0LTdhOGE5MTljLTcwNmItNDQxNS04ZjU1LWUxYmYzMTlkMTRjMy5wbmciLCJ3aWR0aCI6Ijw9NjM2In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.2e2uozU5U7x5MTA7E2OMe-Idx8tywG9XYsy8jRJHxsM', 'name': 'W. Golden Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddx0132-654759fa-357e-411a-b431-50410c392642.png/v1/fill/w_724,h_674,strp/fnaf_2_shadow_freddy_full_body_by_enderziom2004_ddx0132-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Njc0IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZHgwMTMyLTY1NDc1OWZhLTM1N2UtNDExYS1iNDMxLTUwNDEwYzM5MjY0Mi5wbmciLCJ3aWR0aCI6Ijw9NzI0In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.eXRSKwVVykbV_fyxoKLqA6HXF4sYcixl2PFvU6HgkBU', 'name': 'Shadow Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c2a9ca4b-c488-4134-8217-ebc444ec74c0/dfp7p9x-616f3d2f-9a49-444f-8c58-4d036425c0b0.png/v1/fill/w_1280,h_1918/fnaf_2_shadow_bonnie_c4d_render_by_puchaolxd_dfp7p9x-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkxOCIsInBhdGgiOiJcL2ZcL2MyYTljYTRiLWM0ODgtNDEzNC04MjE3LWViYzQ0NGVjNzRjMFwvZGZwN3A5eC02MTZmM2QyZi05YTQ5LTQ0NGYtOGM1OC00ZDAzNjQyNWMwYjAucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.vSyZIVaVi0m9wULYNQUGKtYM8pC5QpMTcpSzHamJ11A', 'name': 'Shadow Bonnie'}
        ]
    }, 
       

    'FNAF 3': {
        'title': "Five Nights at Freddy's 3 (2/3/2015)",
        'protagonist': 'Michael Afton',
        'content': '30 năm sau khi FNAF 1 đóng cửa. Một khu giải trí kinh dị được dựng lại. Bạn đối đầu với Springtrap – chính là kẻ đứng sau mọi sự kiện, William Afton trong bộ đồ Springlock thối rửa sát thịt.',
        'gameplay': 'Chỉ có duy nhất 1 kẻ thù thực sự (Springtrap). Bạn phải dùng âm thanh giả để dụ hắn đi xa khỏi phòng bảo vệ. Phải sửa lỗi hệ thống (Video, Audio, Ventilation) liên tục để tránh bị ảo giác bởi lũ Phantoms và sinh tồn đến 6 giờ sáng.',
        'all_animatronics': 'Springtrap, Phantom Freddy, Phantom Chica, Phantom Foxy, Phantom Puppet, Phantom BB, Phantom Mangle.',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/354140/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=hdHlIy0W4uU',
        'jumpscare_audio': 'https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptoken=d19b7a42-706a-4938-963a-79659b84177d',
        'gallery': [
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8bcf9dce-660a-4cb1-83e6-33e92753acd6/djfsxxd-6ae534cb-97c7-4ac8-8dd7-9f56e4f9b919.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhiY2Y5ZGNlLTY2MGEtNGNiMS04M2U2LTMzZTkyNzUzYWNkNlwvZGpmc3h4ZC02YWU1MzRjYi05N2M3LTRhYzgtOGRkNy05ZjU2ZTRmOWI5MTkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.F5ZqbRp1U1fQccLIlaHMtznTtPHOlEBFykfXc4Zb99M', 'name': 'Springtrap'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8bcf9dce-660a-4cb1-83e6-33e92753acd6/djft17n-6fcfd268-ab53-4eed-9322-f912788170c6.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhiY2Y5ZGNlLTY2MGEtNGNiMS04M2U2LTMzZTkyNzUzYWNkNlwvZGpmdDE3bi02ZmNmZDI2OC1hYjUzLTRlZWQtOTMyMi1mOTEyNzg4MTcwYzYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Wz8s1i-CtJKJsBit25VLzAsHdoMWqPuUvaat8MGruY8', 'name': 'P. Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddlun2s-78a9444c-cd25-4eb2-8b98-59a59b2e6d7b.png/v1/fill/w_606,h_967/fnaf_3_phantom_chica_full_body_by_enderziom2004_ddlun2s-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTY3IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZGx1bjJzLTc4YTk0NDRjLWNkMjUtNGViMi04Yjk4LTU5YTU5YjJlNmQ3Yi5wbmciLCJ3aWR0aCI6Ijw9NjA2In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.fPGUT0WbN0HbhYWYuG3GjB9am4aMq5Y7-2DVRduvmPA', 'name': 'P. Chica'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8bcf9dce-660a-4cb1-83e6-33e92753acd6/djft5qr-2e66ca01-802f-4b09-bcce-8f6eb00bb9d9.png/v1/fill/w_656,h_1218/fnaf_3_phantom_foxy_full_body_by_whfww_djft5qr-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ2MCIsInBhdGgiOiJcL2ZcLzhiY2Y5ZGNlLTY2MGEtNGNiMS04M2U2LTMzZTkyNzUzYWNkNlwvZGpmdDVxci0yZTY2Y2EwMS04MDJmLTRiMDktYmNjZS04ZjZlYjAwYmI5ZDkucG5nIiwid2lkdGgiOiI8PTc4NyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.vcPEFG4amfBVyHn5k-3Q3FZ9wyqYBbKXLAydH6wBhXk', 'name': 'P. Foxy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/599743c7-9070-437a-bf99-ab244f60455b/dfwq2uk-157c9c0b-c935-4b95-a208-b9082ac830b7.png/v1/fill/w_548,h_1457/_fnaf3_sfm__phantom_puppet_by_zoinkeesuwu_dfwq2uk-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzQwMSIsInBhdGgiOiJcL2ZcLzU5OTc0M2M3LTkwNzAtNDM3YS1iZjk5LWFiMjQ0ZjYwNDU1YlwvZGZ3cTJ1ay0xNTdjOWMwYi1jOTM1LTRiOTUtYTIwOC1iOTA4MmFjODMwYjcucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.HpU8bMNwGLJpR1bc0KvupeqkXhTowxNMrgVJsJemvZo', 'name': 'P. Puppet'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddn917o-15f7cc74-70cb-4444-84ae-71d315bf23c1.png/v1/fill/w_347,h_562/fnaf_3_phantom_bb_full_body_by_enderziom2004_ddn917o-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTYyIiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZG45MTdvLTE1ZjdjYzc0LTcwY2ItNDQ0NC04NGFlLTcxZDMxNWJmMjNjMS5wbmciLCJ3aWR0aCI6Ijw9MzQ3In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.3LQZ9dqIrTDgoVSHT0Kd3R5ELuY0pDPlvUZngEHEKY8', 'name': 'P. BB'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddl6pby-dd78073c-bb70-4451-8515-736086239a89.png/v1/fill/w_596,h_807,strp/fnaf_3_phantom_mangle_full_body_by_enderziom2004_ddl6pby-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODA3IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZGw2cGJ5LWRkNzgwNzNjLWJiNzAtNDQ1MS04NTE1LTczNjA4NjIzOWE4OS5wbmciLCJ3aWR0aCI6Ijw9NTk2In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.PwACTByAbAXWC-zZscry_BJ87i0oi53oWQP5T7ghBl0', 'name': 'P. Mangle'}
        ]
    },
    'FNAF 4': {
        'title': "Five Nights at Freddy's 4 (31/10/2015)",
        'protagonist': 'chưa xác định rõ (có thể là The Crying Child hoặc Michael Afton)',
        'content': 'Diễn ra trong phòng ngủ của một đứa trẻ vào năm 1983. Những con Animatronics giờ đây trở thành quái vật ác mộng (Nightmares). Đây là khởi nguồn của tấn bi kịch gia đình Afton.',
        'gameplay': 'Không có camera. Bạn phải dùng tai để nghe tiếng thở ở hai bên cửa. Nếu nghe tiếng thở, phải đóng cửa ngay. Nếu im lặng, mới được bật đèn pin. Chú ý kiểm tra gầm giường và tủ quần áo. Sinh tồn đến 6 giờ sáng.',
        'all_animatronics': 'Nightmares, Jack-O Series, Nightmarionne, N. BB, N. Mangle, Plushtrap.',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/388090/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=A-taWymx1WI',
        'jumpscare_audio': 'https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptoken=3c042940-023b-4899-8086-538466657989',
        'gallery': [
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/dd819fq-cacfc2a4-1b5d-43df-9bd1-001e76fc1e37.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGQ4MTlmcS1jYWNmYzJhNC0xYjVkLTQzZGYtOWJkMS0wMDFlNzZmYzFlMzcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.4IFqcvYOhoIJVMSyPX6RbaTH9Ch3sb_6he22MZ3dsoI', 'name': 'N. Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/dd6qaqz-e775f244-15b0-41c6-8b8c-100cec361dbe.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGQ2cWFxei1lNzc1ZjI0NC0xNWIwLTQxYzYtOGI4Yy0xMDBjZWMzNjFkYmUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.LK5q98XLkkoPLSx6PjlWqt-8V6Iv2ZpkoHDBMWecsL0', 'name': 'N. Bonnie'},
            {'url': 'https://pre00.deviantart.net/d85c/th/pre/f/2015/272/2/6/hq_nightmare_chica_by_manglethefoxtoy-d9bceiu.png', 'name': 'N. Chica'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddqpdt0-63a6d793-ae82-4172-8b21-1f1101cdabe0.png/v1/fill/w_612,h_986,strp/fnaf_4_nightmare_foxy_full_body_by_enderziom2004_ddqpdt0-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTg2IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZHFwZHQwLTYzYTZkNzkzLWFlODItNDE3Mi04YjIxLTFmMTEwMWNkYWJlMC5wbmciLCJ3aWR0aCI6Ijw9NjEyIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.gcFy81d0pyzfduyK0yylZsm_XvW1uG1KMjPNDQXNkqY', 'name': 'N. Foxy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/dbf11371-64c5-4bbc-ae69-9e745fd05ee0/dgsj3a0-af540c02-03d9-496a-87f7-e2ecb09104d5.png/v1/fill/w_1280,h_1280/_fnaf_hw_c4d_render__nightmare_fredbear_by_fredd2055_dgsj3a0-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2RiZjExMzcxLTY0YzUtNGJiYy1hZTY5LTllNzQ1ZmQwNWVlMFwvZGdzajNhMC1hZjU0MGMwMi0wM2Q5LTQ5NmEtODdmNy1lMmVjYjA5MTA0ZDUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.4cXlzG1SDVu9hDZXQZm9uODkr3rwZhU3up5QWvGWun0', 'name': 'N. Fredbear'},
            {'url': 'https://i.pinimg.com/originals/59/69/a0/5969a07c77fd0fda06228aee7f675e78.png', 'name': 'Nightmare'},
            {'url': 'https://vignette.wikia.nocookie.net/fnaf-the-novel/images/1/16/Plushtrap.png/revision/latest?cb=20200323034652', 'name': 'Plushtrap'},
            {'url': 'https://i.pinimg.com/originals/45/1f/ae/451faeb8a7099499e2f03e5ff1fc2124.png', 'name': 'Jack-O-Bonnie'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6d313138-65c7-4b7d-9d13-14195affde2d/defj7fh-e0ad33b6-e8b8-4a83-99b5-e884111920f1.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzZkMzEzMTM4LTY1YzctNGI3ZC05ZDEzLTE0MTk1YWZmZGUyZFwvZGVmajdmaC1lMGFkMzNiNi1lOGI4LTRhODMtOTliNS1lODg0MTExOTIwZjEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.IliYRc75dGLVywENJLC7gRoY60EVGT61K6bvu2P4DE0', 'name': 'Jack-O-Chica'},
            {'url': 'https://orig00.deviantart.net/a621/f/2016/144/1/3/fnaf_4_halloween_edition_nightmarionne_full_body_by_fnatirfanfullbodies-da3noly.png', 'name': 'Nightmarionne'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddw3j12-b264c0ad-9721-43f9-9cca-e2af91ca4c25.png/v1/fill/w_600,h_663,strp/fnaf_4_nightmare_bb_full_body_by_enderziom2004_ddw3j12-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjYzIiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZHczajEyLWIyNjRjMGFkLTk3MjEtNDNmOS05Y2NhLWUyYWY5MWNhNGMyNS5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.C0w01lMUSwqu_Az_zh2jldBqa70xifjHSypXDEWMWnU', 'name': 'N. BB'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f7612dc6-4826-4078-8883-36727ced05ba/djur5mm-0d8aef19-c761-4a86-8c45-1d7dab9488e3.png/v1/fill/w_1280,h_1396/fnaf_4_nightmare_mangle_full_body_by_gaalvatron_djur5mm-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM5NiIsInBhdGgiOiJcL2ZcL2Y3NjEyZGM2LTQ4MjYtNDA3OC04ODgzLTM2NzI3Y2VkMDViYVwvZGp1cjVtbS0wZDhhZWYxOS1jNzYxLTRhODYtOGM0NS0xZDdkYWI5NDg4ZTMucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.fJ62AYdAKGAhLFI8jreypRwPgzkLic48i15W57Gg4-M', 'name': 'N. Mangle'}
        ]
    },
    'Sister Location': {
        'title': "FNAF: Sister Location (7/10/2016)",
        'protagonist': 'Michael Afton',
        'content': 'Michael xuống hầm ngầm của cha mình (William) để tìm hiểu bí mật của ông ta và cái chết của em gái (Elizabeth). Tại đây cậu đối mặt với bí mật ẩn dấu về các con Animatronics',
        'gameplay': 'Lối chơi theo cốt truyện (Story-driven). Mỗi đêm là một nhiệm vụ khác nhau: bò qua phòng tối, sửa chữa bảng điện, hoặc đánh lừa Animatronics bằng thính giác thay vì chỉ ngồi yên một chỗ.',
        'all_animatronics': 'Funtimes, Baby, Ballora, Ennard, Lolbit, Yenndo, Bon-Bon, Bonnet, Minireenas, Bidybabs.',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/506610/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=Uw4-bZkxyKQ&list=PLIfD8qlAXjPVgQIQyLaw4alv15uje335i&index=10',
        'jumpscare_audio': 'https://rpg.hamsterrepublic.com/ohrrpgce-static/6/62/FNAF_Scream.mp3',
        'gallery': [
            {'url': 'https://i.pinimg.com/originals/19/a3/72/19a372604d6a5cdde53012622180b6b5.png', 'name': 'Circus Baby'},
            {'url': 'https://tse2.mm.bing.net/th/id/OIP.B77OMh-aq4dnvbbrHX0YrwHaK2?pid=Api&h=220&P=0', 'name': 'F. Freddy'},
            {'url': 'https://i.pinimg.com/originals/ce/44/e8/ce44e89a67fac359a9cb4753b6964401.png', 'name': 'F. Foxy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/104349e8-1ed2-454a-a787-effc958deac7/df87uei-72fcafb1-99db-49c9-9504-03419e1d8c05.png/v1/fill/w_1280,h_1280/_fnaf___c4d__ballora_by_rexybejar_df87uei-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzEwNDM0OWU4LTFlZDItNDU0YS1hNzg3LWVmZmM5NThkZWFjN1wvZGY4N3VlaS03MmZjYWZiMS05OWRiLTQ5YzktOTUwNC0wMzQxOWUxZDhjMDUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.nxGI_eYQUtzT5I8W8f_hN34Fek1iVQob--HCUPLoxUY', 'name': 'Ballora'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/599743c7-9070-437a-bf99-ab244f60455b/dg1cpsk-a678f4c5-3f2c-4010-aae4-ac80bcae714d.png/v1/fill/w_1280,h_1536/_fnafsl_sfm__bon_bon_by_zoinkeesuwu_dg1cpsk-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUzNiIsInBhdGgiOiJcL2ZcLzU5OTc0M2M3LTkwNzAtNDM3YS1iZjk5LWFiMjQ0ZjYwNDU1YlwvZGcxY3Bzay1hNjc4ZjRjNS0zZjJjLTQwMTAtYWFlNC1hYzgwYmNhZTcxNGQucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.juJ5zQmX4RN9_KTk5nAYwlZ_gzktcO2NAU2G9VNYf3Y', 'name': 'Bon-Bon'},
            {'url': 'https://vignette.wikia.nocookie.net/triple-a-fazbear/images/d/d3/Lolbit.png/revision/latest?cb=20190810141853', 'name': 'Lolbit'},
            {'url': 'https://vignette.wikia.nocookie.net/freddy-fazbears-pizza/images/7/7b/1529.png/revision/latest?cb=20161014023150', 'name': 'Yenndo'},
            {'url': 'https://cdn.comic.studio/images/51310/customs/1722305747116.7974e3b66c709f706612c913455afa8b.png', 'name': 'Bonnet'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddqrrlz-5333e0fa-5276-4b39-bccf-0fda147fc118.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyZTlhZWZjLWI1MDItNDIyZi05OWNlLTU4MGJhNzhhN2Y3YlwvZGRxcnJsei01MzMzZTBmYS01Mjc2LTRiMzktYmNjZi0wZmRhMTQ3ZmMxMTgucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.fazu4Xen3w6RN8QLzRp5mBAkP5R4f5Sne3eIcJ4ICQM', 'name': 'Ennard'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3d352118-95da-4c5d-942c-50a9a68b9d0a/dck5da9-797f2044-9a38-49b5-9551-bf65d8f17546.png/v1/fill/w_800,h_600/minireena___fnaf_collab_the_purplepixel_by_themisteryjulien_dck5da9-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjAwIiwicGF0aCI6IlwvZlwvM2QzNTIxMTgtOTVkYS00YzVkLTk0MmMtNTBhOWE2OGI5ZDBhXC9kY2s1ZGE5LTc5N2YyMDQ0LTlhMzgtNDliNS05NTUxLWJmNjVkOGYxNzU0Ni5wbmciLCJ3aWR0aCI6Ijw9ODAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.j5Bl6KBbZQ3nVimZkJKJ2Wr_9PQyDhT9S-lyblAJftg', 'name': 'Minireena'},
            {'url': 'https://vignette.wikia.nocookie.net/fnaf-world-fanon/images/b/b5/Bidybab_mugshot_edit_full_body_by_joltgametravel-dakcg1u.png/revision/latest?cb=20170723172811&path-prefix=es', 'name': 'Bidybab'}
        ]
    },
    'FFPS (FNAF 6)': {
        'title': "Pizzeria Simulator (2017)",
        'protagonist': 'Michael Afton',
        'content': 'Michael cùng Henry Emily dựng lên một nhà hàng giả để thu hút tất cả các linh hồn còn sót lại (Scrap Baby, Molten Freddy, Scraptrap, Lefty) vào một nơi duy nhất để giải thoát tất cả, chấm dứt nổi đau đớn một lần.',
        'gameplay': 'Sáng làm chủ tiệm Pizza (mua đồ, quảng cáo, Animatronics). Đêm làm việc văn phòng trong ống dẫn khí. Bạn phải tắt quạt và dùng máy dụ âm thanh để kẻ thù không biết vị trí của mình.',
        'all_animatronics': 'Scraps, Rockstars, Mediocre Melodies, Posh Pizza, Trash & Gang, Support Units.',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/738060/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=EGTROsvPivI&list=PLIfD8qlAXjPVgQIQyLaw4alv15uje335i&index=12',
        'jumpscare_audio': 'https://rpg.hamsterrepublic.com/ohrrpgce-static/6/62/FNAF_Scream.mp3',
        'gallery': [
            # Scraps
            {'url': 'https://tse1.mm.bing.net/th/id/OIP.X90_rO1hIsIuA666IlPFiAHaHa?pid=Api&h=220&P=0', 'name': 'Scrap Baby'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a4e0ade1-49b9-4ac5-b8cc-d9d4a3a2941a/ddj7e36-a29dfa94-03a0-4877-85a1-0da5460b1714.png/v1/fill/w_894,h_894,strp/molten_freddy__fnaf_c4d__by_moisogs_ddj7e36-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDA5NiIsInBhdGgiOiJcL2ZcL2E0ZTBhZGUxLTQ5YjktNGFjNS1iOGNjLWQ5ZDRhM2EyOTQxYVwvZGRqN2UzNi1hMjlkZmE5NC0wM2EwLTQ4NzctODVhMS0wZGE1NDYwYjE3MTQucG5nIiwid2lkdGgiOiI8PTQwOTYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.I3Q6epOnn9ruF-Fp0LbD5WsKbo3xx-L1PhqWwLoPXPU', 'name': 'Molten Freddy'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1ea08e12-847b-4c43-8433-ff86b833fd7b/dggl7er-2c65ffd6-3768-4845-ac28-56e24764d837.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFlYTA4ZTEyLTg0N2ItNGM0My04NDMzLWZmODZiODMzZmQ3YlwvZGdnbDdlci0yYzY1ZmZkNi0zNzY4LTQ4NDUtYWMyOC01NmUyNDc2NGQ4MzcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.GiVPswfxS4hf-YFQIm3KCWlhgfTeD4FbGsNQuGHJACc', 'name': 'Scraptrap'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1be59a16-384a-47d2-b9b7-a2baf4d456d0/dkgumqt-f3027382-b847-4b78-9493-dde208f7a02a.png/v1/fill/w_600,h_1000/_fnaf_blender__lefty_render_2_by_tjtheredgator_dkgumqt-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAwMCIsInBhdGgiOiIvZi8xYmU1OWExNi0zODRhLTQ3ZDItYjliNy1hMmJhZjRkNDU2ZDAvZGtndW1xdC1mMzAyNzM4Mi1iODQ3LTRiNzgtOTQ5My1kZGUyMDhmN2EwMmEucG5nIiwid2lkdGgiOiI8PTYwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.DM_rIYJrMwJnArBfx65nEKcV92EPjDprFTI9Ys6Qez8', 'name': 'Lefty'},
            # Rockstars
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2c2dd060-3b1d-4ab1-af82-b3bf9b853993/dcvqz7l-cf223eb2-ae50-472e-81da-e4fec245a170.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJjMmRkMDYwLTNiMWQtNGFiMS1hZjgyLWIzYmY5Yjg1Mzk5M1wvZGN2cXo3bC1jZjIyM2ViMi1hZTUwLTQ3MmUtODFkYS1lNGZlYzI0NWExNzAucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.JF55GDGmuFN1DYNzj4tg9Hn4qJljgUXR-E6FQlFefpE', 'name': 'R. Freddy'},
            {'url': 'https://tse3.mm.bing.net/th/id/OIP.nM5oSDpayIhTfKNonf_xggHaHa?pid=Api&h=220&P=0', 'name': 'R. Bonnie'},
            {'url': 'https://wallpapercave.com/wp/wp9794967.png', 'name': 'R. Chica'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2c2dd060-3b1d-4ab1-af82-b3bf9b853993/dcvjqvu-0e8c8e84-767d-4e76-8f1b-634af27c133a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJjMmRkMDYwLTNiMWQtNGFiMS1hZjgyLWIzYmY5Yjg1Mzk5M1wvZGN2anF2dS0wZThjOGU4NC03NjdkLTRlNzYtOGYxYi02MzRhZjI3YzEzM2EucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.aTA_06vw5wjLD5uRI-t1SR7Q4ul5VpJcCC_pJPGGLc4', 'name': 'R. Foxy'},
            # Mediocre Melodies
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2c2dd060-3b1d-4ab1-af82-b3bf9b853993/dcuf3ss-9f696472-7ae7-4dfe-afcf-1d271146fe51.png/v1/fill/w_894,h_894,strp/happy_frog_fullbody____fnaf_6_ffps__by_chuizaproductions_dcuf3ss-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE2MCIsInBhdGgiOiJcL2ZcLzJjMmRkMDYwLTNiMWQtNGFiMS1hZjgyLWIzYmY5Yjg1Mzk5M1wvZGN1ZjNzcy05ZjY5NjQ3Mi03YWU3LTRkZmUtYWZjZi0xZDI3MTE0NmZlNTEucG5nIiwid2lkdGgiOiI8PTIxNjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.sT95Gzrs4Duj-qE8bX-hMJGTw044K2Au9lvOpfeg0uQ', 'name': 'Happy Frog'},
            {'url': 'https://vignette.wikia.nocookie.net/freddy-fazbears-pizzeria-simulator/images/b/ba/MrHippo.png/revision/latest?cb=20171206011944', 'name': 'Mr. Hippo'},
            {'url': 'https://tse2.mm.bing.net/th/id/OIP.aeg2w3OXBFx85hIKidnfEwHaGA?pid=Api&h=220&P=0', 'name': 'Pigpatch'},
            {'url': 'https://vignette.wikia.nocookie.net/freddy-fazbears-pizza/images/c/cc/FFPS_Nedd_Bear_Model.png/revision/latest?cb=20171209194633', 'name': 'Nedd Bear'},
            {'url': 'https://vignette.wikia.nocookie.net/fredbears-pizzeria/images/e/e8/OrvilleFredbearManagment.png/revision/latest/scale-to-width-down/2000?cb=20190205072312', 'name': 'Orville Elephant'},
            # Posh Pizza
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddldk22-2a5ffb78-9828-4a49-b3d8-558f1b9547b8.png/v1/fill/w_600,h_984,strp/fnaf_6_funtime_chica_full_body_by_enderziom2004_ddldk22-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTg0IiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZGxkazIyLTJhNWZmYjc4LTk4MjgtNGE0OS1iM2Q4LTU1OGYxYjk1NDdiOC5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.MUgDiJm8mm9GdQsyKAj8B0BuN3z-eTDeLUT0XSG4fI8', 'name': 'Funtime Chica'},
            {'url': 'https://tse4.mm.bing.net/th/id/OIP.DEmJbXqg7dMEYaPFF6yVcwHaKe?pid=Api&h=220&P=0', 'name': 'Music Man'},
            {'url': 'https://www.pngkey.com/png/detail/186-1864693_el-chip-fnaf-6-el-chip.png', 'name': 'El Chip'},
            # Support/Vendor/Items
            {'url': 'https://media.tenor.com/vi3LAGPBsLIAAAAC/helpy-fnaf-helpy.gif', 'name': 'Helpy'},
            {'url': 'https://www.pngkey.com/png/detail/112-1129559_confetti-clipart-fnaf-fnaf-6-security-puppet.png', 'name': 'Security Puppet'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12e9aefc-b502-422f-99ce-580ba78a7f7b/ddnlhls-424b981e-3925-4e96-a3b7-795f529875cc.png/v1/fill/w_450,h_571/fnaf_6_candy_cadet_full_body_by_enderziom2004_ddnlhls-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTcxIiwicGF0aCI6IlwvZlwvMTJlOWFlZmMtYjUwMi00MjJmLTk5Y2UtNTgwYmE3OGE3ZjdiXC9kZG5saGxzLTQyNGI5ODFlLTM5MjUtNGU5Ni1hM2I3LTc5NWY1Mjk4NzVjYy5wbmciLCJ3aWR0aCI6Ijw9NDUwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.Z7HTHwxJpD9BwSPBdW9L9sIKRSF2yRywEtdo8caYBe4', 'name': 'Candy Cadet'},
            {'url': 'https://tse3.mm.bing.net/th/id/OIP.hkLty-tXua_rRUbfscRxrwAAAA?pid=Api&h=220&P=0', 'name': 'Mr Hugs'},
            {'url': 'https://vignette.wikia.nocookie.net/pizzaria-freddy-fazbear/images/4/42/Bucket_Bob.png/revision/latest?cb=20171210032858&path-prefix=pt-br', 'name': 'Bucket Bob'},
            {'url': 'https://m.gjcdn.net/fireside-post-image/900/15255455-niujzkai-v4.png', 'name': 'Pan Stan'},
            {'url': 'https://tse2.mm.bing.net/th/id/OIP.S2tx-u9wuRzKlt8eIjJw0AAAAA?pid=Api&h=220&P=0', 'name': 'No. 1 Crate'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c00f8301-14ef-4cae-bb74-fa9f19b15a4a/dhxv0uz-0f7d6498-c0ac-4f5f-8296-7d58b8d86833.png/v1/fill/w_1280,h_1771/mr_can_do_by_austinart404_dhxv0uz-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc3MSIsInBhdGgiOiJcL2ZcL2MwMGY4MzAxLTE0ZWYtNGNhZS1iYjc0LWZhOWYxOWIxNWE0YVwvZGh4djB1ei0wZjdkNjQ5OC1jMGFjLTRmNWYtODI5Ni03ZDU4YjhkODY4MzMucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Eg7WGyY_KxdadJc-BeABreCC2xIk5CTTTZxujGDiLcI', 'name': 'Mr. Can-do'}
        ]
    },
    'UCN': {
        'title': "Ultimate Custom Night (2018)",
        'protagonist': 'William Afton',
        'content': 'nổi đau khổ vĩnh hằng của William được gây ra bởi Cassidy(1 trong nhiều nạn nhân của thắng). địa ngục nơi thắng bị giữ lại trong một cơn ác mộng vĩnh hằng, nơi ông phải đối đầu với tất cả các sáng tạo của mình.',
        'gameplay': 'Tùy chọn 50 nhân vật với độ khó từ 0-20. Bạn phải quản lý điện, nhiệt độ, tiếng ồn, ống dẫn và 2 hệ thống camera cùng một lúc. Đây là bài kiểm tra kỹ năng cao nhất của series.',
        'all_animatronics': 'OMC, Fredbear, Dee Dee, XOR, Phone Guy.',
        'main_img': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/871720/capsule_616x353.jpg',
        'video': 'https://www.youtube.com/watch?v=5jr8Rva4SDY&list=PLIfD8qlAXjPVgQIQyLaw4alv15uje335i&index=15',
        'jumpscare_audio': 'https://images.wikia.nocookie.net/freddy-fazbears-pizzeria-simulator/images/e/ed/Jumpscare_UCN.ogg',
        'gallery': [
            {'url': 'https://vignette.wikia.nocookie.net/freddy-fazbears-pizzeria-simulator/images/a/ab/Old_Man_ConsequencesCN.png/revision/latest?cb=20180622024308', 'name': 'Old Man Consequences (OMC)'},
            {'url': 'https://i.pinimg.com/originals/5a/0c/2e/5a0c2eab258c526b9756773ecd134a97.png', 'name': 'Fredbear'},
            {'url': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/599743c7-9070-437a-bf99-ab244f60455b/dfa3pws-69fec533-1a77-47c1-98ed-744a7776b0bc.png/v1/fill/w_1280,h_1181,strp/_fnaf_world_sfm__adventure_dee_dee_by_zoinkeesuwu_dfa3pws-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE4MSIsInBhdGgiOiJcL2ZcLzU5OTc0M2M3LTkwNzAtNDM3YS1iZjk5LWFiMjQ0ZjYwNDU1YlwvZGZhM3B3cy02OWZlYzUzMy0xYTc3LTQ3YzEtOThlZC03NDRhNzc3NmIwYmMucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Jy-KoPaTSOo3O7VK7GOY0Ez_N9GmIQQ24B_7cVLMLDM', 'name': 'Dee Dee'},
            {'url': 'https://vignette.wikia.nocookie.net/fnaf-ucn/images/6/6c/XOR.png/revision/latest?cb=20200225131144', 'name': 'XOR (Shadow Dee Dee)'},
            {'url': 'https://tse3.mm.bing.net/th/id/OIP.G5S_ORccdLLds6tPTtE60wAAAA?pid=Api&h=220&P=0', 'name': 'Phone Guy'}
        ]
    }
}


 

# --- GIAO DIỆN ---
with st.sidebar:
    st.title('📂 Fazbear Central Database')
    st.markdown("Hệ thống lưu trữ dữ liệu các thực thể Animatronics từ 1983 - 2023.")
    st.markdown("---")
    
    # Menu chọn phiên bản
    selected_version = st.radio("Chọn phiên bản để truy xuất:", list(fnaf_data.keys()))

if selected_version:
    data = fnaf_data[selected_version]
    
    # Phần Header
    st.header(f"🗃️ Hồ sơ: {data['title']}")
    
    col_desc, col_poster = st.columns([1.5, 1])
    with col_desc:
        st.subheader("👤 Nhân vật nhập vai")
        st.info(data['protagonist'])
        st.subheader("📝 Tóm tắt nội dung")
        st.write(data['content'])
        st.write(f"**Cơ chế sinh tồn:** {data['gameplay']}")
        st.subheader("Danh sách Animatronics")
        st.code(data['all_animatronics'])
    
    with col_poster:
        st.image(data['main_img'], use_container_width=True)
        st.subheader("🔊 Tài liệu âm thanh")
        st.audio(data['jumpscare_audio'])
        st.caption("Âm thanh Jumpscare ghi nhận tại hiện trường.")

    st.markdown("---")
    
    # Phần Gallery (Lưới 4 cột)
    st.subheader(f"🖼️ Thư viện hình ảnh Animatronics ({len(data['gallery'])} đối tượng)")
    
    images = data['gallery']
    for i in range(0, len(images), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(images):
                with cols[j]:
                    st.image(images[i+j]['url'], caption=images[i+j]['name'], use_container_width=True)

    st.markdown("---")
    
    # Phần Video Trailer
    st.subheader("🎞️ Tư liệu hình ảnh chuyển động (Trailer)")
    st.video(data['video'])

else:
    st.title("Chào mừng đến với Fazbear Archive")
    st.info("Vui lòng chọn một phiên bản ở thanh bên trái để xem dữ liệu chi tiết.")

#kiếm ảnh, video, file âm thanh, và thêm phần tác giả vào mỗi fnaf
#python -m streamlit run main9.py