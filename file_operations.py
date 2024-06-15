import os
import cv2
import json
import docx
import chardet
from PyPDF2 import PdfReader
from PyQt5.QtGui import QPixmap

def load_data(data_file):
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Загруженные данные: {data}")
            return data
    return {}

def save_data(data_file, data):
    try:
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка записи файла {data_file}: {e}")

def load_image(path, placeholder_image):
    for ext in ("jpg", "png"):
        cover_path = os.path.join(path, f"cover.{ext}")
        if os.path.exists(cover_path):
            return QPixmap(cover_path)
    return placeholder_image

def load_description(path):
    for ext in ("txt", "md"):
        readme_path = os.path.join(path, f"readme.{ext}")
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as file:
                return file.read()
    return "Описание отсутствует"

def load_text_file(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        return raw_data.decode(encoding)

def load_docx_file(file_path):
    doc = docx.Document(file_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def load_pdf_file(file_path):
    reader = PdfReader(file_path)
    return "".join(page.extract_text() for page in reader.pages)

def create_video_preview(video_path, preview_image_path, time_seconds=20):
    try:
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_number = int(fps * time_seconds)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(preview_image_path, frame)
        cap.release()
    except Exception as e:
        print(f"Ошибка при создании превью: {e}")
