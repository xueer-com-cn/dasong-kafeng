import streamlit as st

st.title("This is my first app")
st.write("hello")
if st.button('Click me!'):
    st.write('Button was clicked!')


# 添加图像
from PIL import Image
img = Image.open("5830.jpg")
st.image(img, width=500)
img = Image.open("1.jpg")
st.image(img, width=500)
img = Image.open("2.jpg")
st.image(img, width=500)
