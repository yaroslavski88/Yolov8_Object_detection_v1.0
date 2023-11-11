from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile

def _display_detected_frames(conf, model, st_frame, image):
 
    res = model.predict(image, conf=conf)

    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )

@st.cache_resource
def load_model(model_path):
    model = YOLO(model_path)
    return model


def infer_uploaded_image(conf, model):
    source_img = st.sidebar.file_uploader(
        label="Выберите изображение...",
        type=("jpg", "jpeg", "png", 'bmp', 'webp')
    )

    col1, col2 = st.columns(2)

    with col1:
        if source_img:
            uploaded_image = Image.open(source_img)
            st.image(
                image=source_img,
                caption="Загруженное изображение",
                use_column_width=True
            )

    if source_img:
        if st.button("Старт"):
            with st.spinner("Запускается..."):
                res = model.predict(uploaded_image,
                                    conf=conf)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]

                with col2:
                    st.image(res_plotted,
                             caption="Обработанное изображение",
                             use_column_width=True)
                    try:
                        with st.expander("Результаты обнаружения"):
                            for box in boxes:
                                st.write(box.xywh)
                    except Exception as ex:
                        st.write("Изображение не загружено")
                        st.write(ex)


def infer_uploaded_video(conf, model):

    source_video = st.sidebar.file_uploader(
        label="Выберите видео..."
    )

    if source_video:
        st.video(source_video)

    if source_video:
        if st.button("Старт"):
            with st.spinner("Запускается..."):
                try:
                    tfile = tempfile.NamedTemporaryFile()
                    tfile.write(source_video.read())
                    vid_cap = cv2.VideoCapture(
                        tfile.name)
                    st_frame = st.empty()
                    while (vid_cap.isOpened()):
                        success, image = vid_cap.read()
                        if success:
                            _display_detected_frames(conf,
                                                     model,
                                                     st_frame,
                                                     image
                                                     )
                        else:
                            vid_cap.release()
                            break
                except Exception as e:
                    st.error(f"Ошибка загрузки видео: {e}")


def infer_uploaded_webcam(conf, model):

    try:
        flag = st.button(
            label="Остановить"
        )
        vid_cap = cv2.VideoCapture(0)
        st_frame = st.empty()
        while not flag:
            success, image = vid_cap.read()
            if success:
                _display_detected_frames(
                    conf,
                    model,
                    st_frame,
                    image
                )
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Ошибка загрузки видео: {str(e)}")