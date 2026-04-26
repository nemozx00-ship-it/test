import streamlit as st
st.title('Điền thông tin giới thiệu bản thân em')
my_bar = st.progress(0)
questions_text = ['Họ và tên:', 'Ngày tháng năm sinh:', 'Sở thích:']
questions_psychology = [
    'Bạn có đang gặp vấn đề tâm lý nào không?', 
    'Bạn có đang thật hạnh phúc không?', 
    'Bạn có muốn rời đi không?'
]
answers = []
for i, q in enumerate(questions_text):
    ans = st.text_input(q, key=f"txt_{i}")
    if ans != '':
        answers.append(ans)
for i, q in enumerate(questions_psychology):
    ans_p = st.radio(q, ['Chưa chọn', 'Có', 'Không'], key=f"psy_{i}")
    if ans_p != 'Chưa chọn':
        answers.append(ans_p)
total_questions = len(questions_text) + len(questions_psychology)
if st.button('Confirm'):
    if len(answers) == total_questions:
        my_bar.progress(100)
        st.success('Bạn đã hoàn thành đầy đủ thông tin!')
        st.balloons()
        st.write('---')
        st.subheader('Tóm tắt thông tin:')
        all_questions = questions_text + questions_psychology
        for q, a in zip(all_questions, answers):
            st.write(f"**{q}** {a}")
    else:
        ti_le = len(answers) / total_questions
        my_bar.progress(ti_le)
        st.warning(f'Bạn mới hoàn thành {len(answers)}/{total_questions} câu hỏi. Vui lòng điền nốt nhé!')
