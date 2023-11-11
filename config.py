from pathlib import Path
import sys

file_path = Path(__file__).resolve()

root_path = file_path.parent

if root_path not in sys.path:
    sys.path.append(str(root_path))

ROOT = root_path.relative_to(Path.cwd())


SOURCES_LIST = ["Изображение", "Видео", "Вебкамера"]

DETECTION_MODEL_DIR = ROOT / 'weights' / 'detection'
DetLicPL_s = DETECTION_MODEL_DIR / "DetLicPL_s.pt"
DetLicPL_l = DETECTION_MODEL_DIR / "DetLicPL_l.pt"
VehDet = DETECTION_MODEL_DIR / "VehDet.pt"
YOLOv8n = DETECTION_MODEL_DIR / "yolov8n.pt"
YOLOv8s = DETECTION_MODEL_DIR / "yolov8s.pt"
YOLOv8m = DETECTION_MODEL_DIR / "yolov8m.pt"
YOLOv8l = DETECTION_MODEL_DIR / "yolov8l.pt"
YOLOv8x = DETECTION_MODEL_DIR / "yolov8x.pt"
YOLOv8n_seg = DETECTION_MODEL_DIR / "yolov8n-seg.pt"
YOLOv8s_seg = DETECTION_MODEL_DIR / "yolov8s-seg.pt"
YOLOv8m_seg = DETECTION_MODEL_DIR / "yolov8m-seg.pt"
YOLOv8l_seg = DETECTION_MODEL_DIR / "yolov8l-seg.pt"
YOLOv8x_seg = DETECTION_MODEL_DIR / "yolov8x-seg.pt"

DETECTION_MODEL_CAR_LIST = [
    "VehDet.pt"]

DETECTION_MODEL_GN_LIST = [
    "DetLicPL_s.pt",
    "DetLicPL_l.pt"]

DETECTION_MODEL_SEG_LIST = [
    "yolov8n-seg.pt",
    "yolov8s-seg.pt",
    "yolov8m-seg.pt",
    "yolov8l-seg.pt",
    "yolov8x-seg.pt"]

DETECTION_MODEL_OTHER_LIST = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolov8m.pt",
    "yolov8l.pt",
    "yolov8x.pt"]

DETECTION_TASK_LIST = [
    "Обнаружение транспорта",
    "Обнаружение гос.номера автомобиля",
    "Сегментация",
    "Обнаружение объектов"]

