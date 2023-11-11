from pathlib import Path
from PIL import Image
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

st.set_page_config(
    page_title="Интерактивный интерфейс для YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )

# заголовок главной страницы
st.title("Интерактивный интерфейс для YOLOv8")

st.sidebar.header("Настройка модели DL")

# опции модели
task_type = st.sidebar.selectbox(
    "Выберите задачу",
    config.DETECTION_TASK_LIST
)


model_type = None
if task_type == "Обнаружение транспорта":
    model_type = st.sidebar.selectbox(
        "Выберите модель",
        config.DETECTION_MODEL_CAR_LIST
    )
elif task_type == "Обнаружение гос.номера автомобиля":
      model_type = st.sidebar.selectbox(
        "Выберите модель",
        config.DETECTION_MODEL_GN_LIST
      )
elif task_type == "Сегментация":
      model_type = st.sidebar.selectbox(
        "Выберите модель",
        config.DETECTION_MODEL_SEG_LIST
      )
elif task_type == "Обнаружение объектов":
      model_type = st.sidebar.selectbox(
        "Выберите модель",
        config.DETECTION_MODEL_OTHER_LIST
      )
else:
    st.error("Другие функции пока не реализованы")

confidence = float(st.sidebar.slider(
    "Выберите уверенность модели", 1, 100, 50)) / 100

model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
else:
    st.error("Пожалуйста, выберите модель на боковой панели")

# загрузка обученной модели
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Не удалось загрузить модель. Пожалуйста, проверьте указанный путь: {model_path}")

# Настройка изображения/видео
st.sidebar.header("Настройка изображения/видео")
source_selectbox = st.sidebar.selectbox(
    "Выберите источник",
    config.SOURCES_LIST
)

source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model)
else:
    st.error("Выберите источник.")
