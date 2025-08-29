from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
import mysql.connector
from tkcalendar import Calendar  # pip install tkcalendar

class AttendanceForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
   
        # Bg Image
        bg_path = os.path.join("images", "login.jpeg")
        self.bg = ImageTk.PhotoImage(file=bg_path)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        left_path = os.path.join("images", "rg2.jpg")
        self.bg1 = ImageTk.PhotoImage(file=left_path)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Variables
        self.branch_var = StringVar()
        self.class_var = StringVar()
        self.division_var = StringVar()
        self.semester_var = StringVar()
        self.time_var = StringVar()
        self.date_var = StringVar()

        # Title
        register_lbl = Label(frame, text="ATTENDANCE HERE", font=("times new roman", 25, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Branch Selection
        branch_lbl = Label(frame, text="Branch:", font=("Helvetica", 14), bg="white")
        branch_lbl.place(x=20, y=80)
        branch_combo = ttk.Combobox(frame, textvariable=self.branch_var, values=["CSE", "Civil", "Mechanical", "ENTC", "Other"], font=("Helvetica", 14), width=18)
        branch_combo.place(x=100, y=80)

        # Class Selection
        class_lbl = Label(frame, text="Class:", font=("Helvetica", 14), bg="white")
        class_lbl.place(x=20, y=150)
        class_combo = ttk.Combobox(frame, textvariable=self.class_var, values=["Class FY", "Class SY", "Class TY", "Class B.Tech"], font=("Helvetica", 14), width=18)
        class_combo.place(x=100, y=180)

        # Division Selection
        division_lbl = Label(frame, text="Division:", font=("Helvetica", 14), bg="white")
        division_lbl.place(x=20, y=220)
        division_combo = ttk.Combobox(frame, textvariable=self.division_var, values=["Division A", "Division B", "Division C"], font=("Helvetica", 14), width=18)
        division_combo.place(x=100, y=250)

        # Semester Selection
        semester_lbl = Label(frame, text="Semester:", font=("Helvetica", 14), bg="white")
        semester_lbl.place(x=20, y=290)
        semester_combo = ttk.Combobox(frame, textvariable=self.semester_var, values=["Semester 1", "Semester 2", "Semester 3", "Semester 4"], font=("Helvetica", 14), width=18)
        semester_combo.place(x=100, y=320)

        # Time Selection
        time_lbl = Label(frame, text="Time:", font=("Helvetica", 14), bg="white")
        time_lbl.place(x=20, y=360)
        time_combo = ttk.Combobox(frame, textvariable=self.time_var, values=["Lecture/Tutorial 10:30 AM - 11:30 AM", "11:30 AM - 12:30 PM", "1:15 PM - 2:15 PM", "2:15 PM - 3:15 PM", "3:30 PM - 4:30 PM", "4:30 PM - 5:30 PM", "Practical 10:30 AM - 12:30 PM", "1:15 PM - 3:15 PM", "3:30 PM - 5:30 PM"], font=("Helvetica", 14), width=18)
        time_combo.place(x=100, y=390)

        # Date Selection
        date_lbl = Label(frame, text="Date:", font=("Helvetica", 14), bg="white")
        date_lbl.place(x=20, y=430)
        date_entry = Entry(frame, textvariable=self.date_var, font=("Helvetica", 14), width=20, bd=2, relief=GROOVE)
        date_entry.place(x=220, y=460)
        calendar_btn = Button(frame, text="Select Date", command=self.select_date, bg="#4CAF50", fg="white", font=("Helvetica", 14), bd=0, relief=FLAT)
        calendar_btn.place(x=100, y=460)

        # Submit Button
        submit_btn = Button(frame, text="Submit", command=self.submit_form, bg="#4CAF50", fg="white", font=("Helvetica", 14), bd=0, relief=FLAT)
        submit_btn.place(x=200, y=500)

    def select_date(self):
        # Open a calendar to select a date
        top = Toplevel(self.root)
        cal = Calendar(top, font="Arial 14", selectmode='day')
        cal.pack(fill="both", expand=True)
        
        def get_date():
            self.date_var.set(cal.get_date())
            top.destroy()
        
        ok_btn = Button(top, text="OK", command=get_date, bg="#4CAF50", fg="white", font=("Helvetica", 14), bd=0, relief=FLAT)
        ok_btn.pack(pady=10)

    def submit_form(self):
        # Get the form data and do something with it
        branch_val = self.branch_var.get()
        class_val = self.class_var.get()
        division_val = self.division_var.get()
        semester_val = self.semester_var.get()
        time_val = self.time_var.get()
        date_val = self.date_var.get()

        # Example: Printing the form data
        print("Branch:", branch_val)
        print("Class:", class_val)
        print("Division:", division_val)
        print("Semester:", semester_val)
        print("Time:", time_val)
        print("Date:", date_val)
        # Here you can insert the data into your database or perform any other action

if __name__ == "__main__":
    root = Tk()
    app = AttendanceForm(root)
    root.mainloop()