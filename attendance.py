import cv2
import numpy as np
import mysql.connector
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pandas as pd
from tkcalendar import DateEntry

class FaceRecognitionAttendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Load known faces and encodings
        self.known_face_encodings = []
        self.known_face_names = []

        self.load_known_faces()

        # Background image
        img3 = Image.open(r"images/login.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=600)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=580)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=710, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("roll", text="Roll")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance Status")

        self.attendance_table["show"] = "headings"

        self.attendance_table.column("id", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("department", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("attendance", width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)

        # Start Attendance Button
        start_attendance_btn = Button(main_frame, text="Start Attendance", command=self.start_attendance, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        start_attendance_btn.place(x=10, y=20)
        
        # Export Attendance Button
        export_attendance_btn = Button(main_frame, text="Export to Excel", command=self.export_to_excel, font=("times new roman", 15, "bold"), bg="green", fg="white")
        export_attendance_btn.place(x=250, y=20)

        export_range_btn = Button(main_frame, text="Export by Date Range", command=self.select_date_range, font=("times new roman", 15, "bold"), bg="green", fg="white")
        export_range_btn.place(x=450, y=20)

    def load_known_faces(self):
        # Load known faces from the database or pre-trained data
        # Placeholder method for loading known face encodings and names
        pass

    def is_student_enrolled(self, roll):
        # Implement logic to check if the student is currently enrolled
        conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
        my_cursor = conn.cursor()
        query = "SELECT * FROM student WHERE Roll=%s"
        my_cursor.execute(query, (roll,))
        row = my_cursor.fetchone()
        conn.close()
        return row is not None

    def should_be_present(self, roll, date, time):
        # Implement logic to check if the student should be present
        # This could be based on class schedules, timetables, or other relevant information
        # For simplicity, let's assume students should be present during school hours (8 AM - 5 PM)
        class_start_time = datetime.strptime("08:00:00", "%H:%M:%S").time()
        class_end_time = datetime.strptime("17:00:00", "%H:%M:%S").time()
        current_time = datetime.strptime(time, "%H:%M:%S").time()
        return class_start_time <= current_time <= class_end_time

    def mark_attendance(self, roll):
        conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
        my_cursor = conn.cursor()
        now = datetime.now()
        d1 = now.strftime("%Y-%m-%d")
        dtString = now.strftime("%H:%M:%S")

        query = "SELECT Student_name, Department FROM student WHERE Roll=%s"
        my_cursor.execute(query, (roll,))
        result = my_cursor.fetchone()
        if result:
            name, department = result
            if self.is_student_enrolled(roll) and self.should_be_present(roll, d1, dtString):
                # Check if attendance has already been marked for the student on the current date
                check_query = "SELECT id FROM attendance WHERE roll=%s AND date=%s"
                my_cursor.execute(check_query, (roll, d1))
                existing_attendance = my_cursor.fetchone()
                if existing_attendance is None:
                    # If attendance has not been marked yet, insert a new record
                    query = "INSERT INTO attendance (roll, name, department, time, date, attendance) VALUES (%s, %s, %s, %s, %s, %s)"
                    my_cursor.execute(query, (roll, name, department, dtString, d1, "Present"))
                    conn.commit()
                else:
                    print(f"Attendance already marked for {name} ({roll}) on {d1}")
        conn.close()

    def start_attendance(self):
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # Load the pre-trained face recognizer

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1)
            if key == 13:  # Press 'Enter' to break the loop
                break
            elif key == ord('q'):  # Press 'q' to quit the application
                break

        video_cap.release()
        cv2.destroyAllWindows()
        self.fetch_data()

    def recognize(self, img, clf, faceCascade):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in features:
            id, predict = clf.predict(gray_image[y:y+h, x:x+w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence > 77:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@123", database="face_recognition_attendance_system")
                cursor = conn.cursor()

                cursor.execute(f"SELECT Student_name, Roll, Department FROM student WHERE Student_Id={id}")
                result = cursor.fetchone()
                if result:
                    name, roll, department = result
                    cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX,0.8, (255, 25, 255), 3)
                    self.mark_attendance(roll)  # Mark attendance for the recognized student
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                conn.close()

        return img

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT attendance.id, attendance.roll, student.Student_name, student.Department, attendance.time, attendance.date, attendance.attendance FROM attendance JOIN student ON attendance.roll = student.Roll")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in data:
                self.attendance_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def export_to_excel(self, start_date=None, end_date=None):
        conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
        my_cursor = conn.cursor()

        if start_date and end_date:
            query = "SELECT attendance.id, attendance.roll, student.Student_name, student.Department, TIME_FORMAT(attendance.time, '%H:%M:%S'), DATE_FORMAT(attendance.date, '%Y-%m-%d'), attendance.attendance FROM attendance JOIN student ON attendance.roll = student.Roll WHERE attendance.date BETWEEN %s AND %s"
            my_cursor.execute(query, (start_date, end_date))
        else:
            my_cursor.execute("SELECT attendance.id, attendance.roll, student.Student_name, student.Department, TIME_FORMAT(attendance.time, '%H:%M:%S'), DATE_FORMAT(attendance.date, '%Y-%m-%d'), attendance.attendance FROM attendance JOIN student ON attendance.roll = student.Roll")

        data = my_cursor.fetchall()
        conn.close()

        if len(data) != 0:
            df = pd.DataFrame(data, columns=["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance Status"])
            df['Time'] = df['Time'].apply(str)  # Convert Timedelta to string
            df.to_excel("Attendance_Report.xlsx", index=False)
            messagebox.showinfo("Export to Excel", "Attendance report has been exported successfully!")
        else:
            messagebox.showwarning("Export to Excel", "No data found to export")
            
    def select_date_range(self):
        def export_range():
            start_date = date_start.get_date()
            end_date = date_end.get_date()
            self.export_to_excel(start_date, end_date)
            date_range_window.destroy()

        date_range_window = Toplevel(self.root)
        date_range_window.title("Select Date Range")
        date_range_window.geometry("300x150")

        date_start_label = Label(date_range_window, text="Start Date:")
        date_start_label.pack(pady=5)
        date_start = DateEntry(date_range_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_start.pack(pady=5)

        date_end_label = Label(date_range_window, text="End Date:")
        date_end_label.pack(pady=5)
        date_end = DateEntry(date_range_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_end.pack(pady=5)

        export_button = Button(date_range_window, text="Export", command=export_range)
        export_button.pack(pady=10)

    
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionAttendance(root)
    root.mainloop()