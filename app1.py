import streamlit as st
import pandas as pd
import numpy as np

# app title
st.title("My first deployed DL model")
st.header("Header đây chứ đâu")
st.text("Đây là text")
st.markdown('Markdown đây **anh em ơi**')
st.text("Còn dưới đây là latex")
st.latex(r''' a + b = 3''')
# Viết một cái gì đó
st.write(12345)

# Hiển thị code luôn
code = '''def(hello):
        print("Hello world!)'''
st.code(code, language='python')

st.text("Hiển thi luôn cả chart")
hart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(hart_data)

# Checkbox
if st.checkbox('Show text'):
        st.write("This is a text")

option = st.selectbox(
    'Select one', ('The option 1', 'The option 2'))

'You selected: ', option