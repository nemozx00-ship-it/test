import streamlit as st
st.set_page_config(
    page_title='Trắc nghiệm tính cách', 
    page_icon=':question:', 
    layout='wide'
)
st.title('Hãy chọn một con vật bạn yêu thích')
Personality = {
    'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được đi nghỉ.',
    'Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra.',
    'Chim đại bàng': 'Bạn là người dũng mãnh, luôn khao khát tự do và có tầm nhìn xa trông rộng để chinh phục những đỉnh cao mới.',
    'Con người': 'Bạn đại diện cho sự phát triển không ngừng và trí thông minh vượt trội. Bạn luôn tìm tòi học hỏi và có khả năng làm chủ vận mệnh của chính mình.',
    'Axolotl': 'Bạn có khả năng thích nghi tuyệt vời với mọi hoàn cảnh, luôn giữ được sự lạc quan và sẵn sàng tái tạo năng lượng cho bản thân.'
}
cols = st.columns(len(Personality))
buttons = {}
for i, animal in enumerate(Personality.keys()):
    with cols[i]:
        buttons[animal] = st.button(animal)
for animal, clicked in buttons.items():
    if clicked:
        with st.expander(animal):
            st.write(Personality[animal])
        with st.sidebar:
            st.title('Trắc nghiệm tính cách')
            st.write(f'Bạn chọn: {animal}')