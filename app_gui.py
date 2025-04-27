import tkinter as tk
from tkinter import messagebox
from dataset_creator import create_dataset
from train_model import train_model
from recognize_attendance import recognize_face

def run_dataset():
    user_id = entry_id.get()
    name = entry_name.get()
    if user_id and name:
        create_dataset(user_id, name)
    else:
        messagebox.showerror("Error", "Please enter both ID and Name")

def run_training():
    train_model()

def run_recognition():
    recognize_face()

root = tk.Tk()
root.title("Face Recognition Attendance System")

tk.Label(root, text="User ID:").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Button(root, text="1. Create Dataset", command=run_dataset).pack(pady=5)
tk.Button(root, text="2. Train Model", command=run_training).pack(pady=5)
tk.Button(root, text="3. Recognize & Mark Attendance", command=run_recognition).pack(pady=5)

root.geometry("300x250")
root.mainloop()