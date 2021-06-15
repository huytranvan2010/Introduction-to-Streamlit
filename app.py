import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request
from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# app title
st.title("My first deployed DL model")

st.text("Đây là text")

st.markdown('Markdown **anh em oi**')

st.text("Còn dưới đây là latex")

st.latex(r''' a + b = 3''')

st.write(12345)

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 90, 30]
}))


image = Image.open('dog.jpg')

# hiển thị image
show = st.image(image, use_column_width=False, width=300)

st.sidebar.title("Upload image")

# Disable warning
st.set_option('deprecation.showfileUploaderEncoding', False)

# chọn ảnh
uploaded_file = st.sidebar.file_uploader(" ", type=['png', 'jpg', 'jpeg'])

# upload xong thì nhấn classify để predict

if st.sidebar.button("Click here to classify"):     # tạo button và nếu nhấn vào đây thì
    if uploaded_file is None:
        st.sidebar.write("please upload an image")
    else:
        image = image.resize((64, 64))
        image = img_to_array(image) / 255.
        image = np.expand_dims(image, axis=0)
        classifier = load_model('DogCat.h5')
        pred = classifier.predict(image)[0][0]
        if pred > 0.5:
            st.write("This is a dog")
        else:
            st.write("This is a cat")
        # predict

# """
# streamlit run app.py
# Nhấn Ctrl + C để thoát
# """