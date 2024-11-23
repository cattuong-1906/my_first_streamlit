import streamlit as st

st.title('Bé tập làm toán')
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('a')
with col2:
    radio = st.radio('Phép toán', ('\+', '\-', 'x', ':'), horizontal  = True)
with col3:
    b = st.number_input('b')
ket_qua = st.number_input('Nhập kết quả')
if st.button('Kiểm tra', use_container_width=True):
    if radio == '\+':
        dap_an = a + b
    elif radio == '\-':
        dap_an = a + b
    elif radio == 'x':
        dap_an = a * b
    elif radio == ':':
        if b == 0:
            st.text('Nhập b sai')
        dap_an = a / b
    
    if dap_an == ket_qua:
        st.success('Chính xác')
        st.balloons()
    else:
        st.error(f'Sai. Đáp án đúng là: {ket_qua}')
        st.snow()