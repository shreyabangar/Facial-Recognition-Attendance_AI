import tkinter as tk 
from tkinter import messagebox 
from dataset_creator import create_dataset 
from train_model import train_model 
from recognize_attendance import recognize_face 
 
def run_dataset(): 
    roll_no = entry_roll.get() 
    name = entry_name.get() 
 
    if not roll_no or not name: 
        messagebox.showerror("Input Error", "Please enter both Roll No and Name.") 
        return 
 
    create_dataset(roll_no, name) 
 
def run_training(): 
    train_model() 
 
import threading 
 
def run_recognition(): 
    thread = threading.Thread(target=recognize_face) 
    thread.daemon = True 
    thread.start() 
 
def exit_app(): 
    print("[INFO] Exiting application...") 
    root.quit() 
    root.destroy() 
 
def styled_button(master, text, command, color, row): 
    btn = tk.Button( 
        master, 
        text=text, 
        command=command, 
        font=("Arial", 10, "bold"), 
        bg=color, 
        fg="white", 
        activebackground="#2c3e50", 
        activeforeground="white", 
        relief="flat", 
        cursor="hand2", 
        bd=0, 
        padx=10, 
        pady=10, 
        width=25 
    ) 
    btn.grid(row=row, column=0, columnspan=2, pady=7) 
    return btn 
 
# GUI setup 
root = tk.Tk() 
root.title("Face Recognition Attendance System") 
root.configure(bg="#ecf0f1") 
root.geometry("500x400") 
root.resizable(False, False) 
 
frame = tk.Frame(root, bg="#ecf0f1") 
frame.pack(expand=True) 
 
# Title 
title_label = tk.Label(frame, text="Facial Recognition Attendance", font=("Arial", 18, "bold"), 
bg="#ecf0f1", fg="#2c3e50") 
title_label.grid(row=0, column=0, columnspan=2, pady=20) 
 
# Roll No 
label_roll = tk.Label(frame, text="Roll No:", font=("Arial", 12), bg="#ecf0f1") 
label_roll.grid(row=1, column=0, sticky="e", padx=10, pady=5) 
entry_roll = tk.Entry(frame, font=("Arial", 12), width=25) 
entry_roll.grid(row=1, column=1, padx=10, pady=5) 
 
# Name 
label_name = tk.Label(frame, text="Name:", font=("Arial", 12), bg="#ecf0f1") 
label_name.grid(row=2, column=0, sticky="e", padx=10, pady=5) 
entry_name = tk.Entry(frame, font=("Arial", 12), width=25) 
entry_name.grid(row=2, column=1, padx=10, pady=5) 
 
# Buttons 
styled_button(frame, "Create Dataset", run_dataset, "#3498db", 3) 
styled_button(frame, "Train Model", run_training, "#27ae60", 4) 
styled_button(frame, "Take Attendance", run_recognition, "#8e44ad", 5) 
styled_button(frame, "Exit", exit_app, "#e74c3c", 6) 
 
root.mainloop()
