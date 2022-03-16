import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import pickle
with open("model.db", 'rb') as f:  # 读取文件
    model = pickle.load(f)  # 导入模型
# 打印标题和副标题
st.title("Number Recognizer")
st.write("Please write a single digit!")
size, resize = 192, 8  # 定义大小和缩放大小
mode = st.checkbox("Draw(or Delete)?", True)
canvas_result = st_canvas(  # 制作画布
    fill_color='#000000',
    stroke_width=20,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=size,
    height=size,
    drawing_mode="freedraw" if mode else "transform",
    key="canvas")

if canvas_result.image_data is not None:  # 处理输入的手写数字
    img = cv2.resize(canvas_result.image_data.astype("uint8"), (resize, resize), interpolation=cv2.INTER_NEAREST)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rescaled = cv2.resize(img, (size, size), interpolation=cv2.INTER_NEAREST)
    st.write("Model Input")
    st.image(rescaled, clamp=True)
if st.button("Predict"):  # 设置可交互按钮
    test_x = img.reshape(1, resize*resize)
    test_x = test_x.tolist()
    val = model.prediction(test_x[0])
    st.title(f'the digit is {val}')
