import cv2
import os

def create_dataset(user_id, name):
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    count = 0

    if not os.path.exists("dataset"):
        os.makedirs("dataset")

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y + h, x:x + w]
            cv2.imwrite(f"dataset/user.{user_id}.{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Creating Dataset", frame)
        if cv2.waitKey(1) == 13 or count >= 50:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Dataset creation complete for {name} with ID: {user_id}")