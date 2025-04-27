import cv2 
import os 
import csv 
from datetime import datetime 
 
def mark_attendance(roll_no): 
    today = datetime.now().strftime("%Y-%m-%d") 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    filepath = "Attendance/attendance.csv" 
 
    if not os.path.exists("Attendance"): 
        os.makedirs("Attendance") 
 
    # Create file with headers 
    if not os.path.exists(filepath): 
        with open(filepath, "w", newline="") as f: 
            writer = csv.writer(f) 
            writer.writerow(["Roll No", "Time"]) 
 
    already_marked = set() 
    with open(filepath, "r") as f: 
        reader = csv.reader(f) 
        next(reader, None) 
        for row in reader: 
            if row and row[1].startswith(today): 
                already_marked.add(row[0]) 
 
    if str(roll_no) not in already_marked: 
        with open(filepath, "a", newline="") as f: 
            writer = csv.writer(f) 
            writer.writerow([roll_no, timestamp]) 
        print(f"[INFO] Marked attendance for Roll No {roll_no}") 
    else: 
        print(f"[INFO] Already marked today: Roll No {roll_no}") 
 
def recognize_face(): 
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read("trainer/trainer.yml") 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
"haarcascade_frontalface_default.xml") 
 
    cap = cv2.VideoCapture(0) 
    print("[INFO] Starting facial recognition...") 
 
    session_marked_ids = set()  # Add this to track marked IDs in the current session 
 
    while True: 
        ret, frame = cap.read() 
        if not ret: 
            print("[ERROR] Failed to grab frame") 
            break 
 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.2, 5) 
 
        for (x, y, w, h) in faces: 
            id_, confidence = recognizer.predict(gray[y:y+h, x:x+w]) 
 
            if confidence < 60: 
                if id_ not in session_marked_ids: 
                    mark_attendance(id_) 
                    session_marked_ids.add(id_) 
                    print(f"[INFO] Attendance marked for Roll No {id_}") 
                label = f"Roll No {id_}" 
            else: 
                label = "Unknown" 
 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) 
            cv2.putText(frame, label, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2) 
 
        cv2.imshow("Recognizing Faces", frame) 
        if cv2.waitKey(1) == 13:  # Press Enter to exit 
            break 
 
    cap.release() 
    cv2.destroyAllWindows()

    
