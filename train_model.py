import cv2
import numpy as np
from PIL import Image
import os

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'dataset'

    def get_images_and_labels(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        faces, ids = [], []

        for image_path in image_paths:
            gray_img = Image.open(image_path).convert('L')
            img_np = np.array(gray_img, 'uint8')
            user_id = int(os.path.split(image_path)[-1].split(".")[1])
            faces.append(img_np)
            ids.append(user_id)

        return faces, np.array(ids)

    faces, ids = get_images_and_labels(path)
    recognizer.train(faces, ids)
    if not os.path.exists("trainer"):
        os.makedirs("trainer")
    recognizer.save("trainer/trainer.yml")
    print("[INFO] Training complete and model saved!")