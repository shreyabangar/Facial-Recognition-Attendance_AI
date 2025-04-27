import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import os
import csv


def mark_attendance(user_id):
    now = datetime.now()
    today_date = now.strftime('%Y-%m-%d')
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists("Attendance"):
        os.makedirs("Attendance")

    filename = "Attendance/attendance.csv"

    # Create file with headers if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Time"])

    # Check if already marked today
    already_marked = False
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row and row[0] == str(user_id) and row[1].startswith(today_date):
                already_marked = True
                break

    # Write only if not already marked today
    if not already_marked:
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([user_id, dt_string])
        print(f"[INFO] Attendance marked for ID {user_id}")
    else:
        print(f"[INFO] Attendance already marked for ID {user_id} today.")

def recognize_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer/trainer.yml")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 60:
                mark_attendance(id_)
                label = f"ID {id_}"
            else:
                label = "Unknown"

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Recognizing...", frame)
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()