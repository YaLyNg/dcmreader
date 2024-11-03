import streamlit as st
import pydicom
import numpy as np
from PIL import Image

#by ai just a test

st.title('DICOM文件查看器')

# 创建一个文件上传器，让用户上传DICOM文件
uploaded_file = st.file_uploader('请选择DICOM文件:',type=['dcm'])

# 检查是否有DICOM文件被上传
if uploaded_file is not None:
    # 将上传的文件转换为DICOM对象
    st.session_state.dicom_image = pydicom.dcmread(uploaded_file)

    # 创建灰度滑块
    gray_scale = st.slider('调整灰度:', min_value=0, max_value=255, value=128, step=1, key='gray_scale')

    # 获取DICOM文件的图像数据
    image_data = st.session_state.dicom_image.pixel_array

    # 应用灰度调整
    image_data = np.clip(image_data, 0, 255)
    image_data = (image_data - 255 / 2) + gray_scale
    image_data = np.clip(image_data, 0, 255)
    image_data = image_data.astype(np.uint8)

    # 显示图像
    st.image(image_data, caption='DICOM图像', use_column_width=True)
    st.write('DICOM文件元数据:')
    st.write(st.session_state.dicom_image)
