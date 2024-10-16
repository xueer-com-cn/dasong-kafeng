import streamlit as st
 
# 添加文本
st.title('Hello, World!')
st.header('This is a Streamlit tutorial')
st.subheader('Introduction to Streamlit')
 
# 添加图像
from PIL import Image
img = Image.open("5830.jpg")
st.image(img, width=500)
img = Image.open("1.jpg")
st.image(img, width=500)
img = Image.open("2.jpg")
st.image(img, width=500)

 
# 运行应用程序
if __name__ == '__main__':
    st.write('This is a Streamlit tutorial')
