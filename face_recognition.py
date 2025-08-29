from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import mysql.connector

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images/face1.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_top1 = Image.open(r"images/face.jpeg")
        img_top1 = img_top1.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl1 = Label(self.root, image=self.photoimg_top1)
        f_lbl1.place(x=650, y=55, width=950, height=700)

        btn1 = Button(f_lbl1, text="Face Recognition", command=self.face_recognition, width=36, font=("times new roman", 18, "bold"), bg="green", fg="white")
        btn1.place(x=350, y=615, width=250, height=40)

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="root@123", database="face_recognition_attendance_system")
                cursor = conn.cursor()

                cursor.execute(f"SELECT Student_name FROM student WHERE Student_Id={id}")
                name = cursor.fetchone()
                name = "+".join(name) if name else "Unknown"
                
                cursor.execute(f"SELECT Roll FROM student WHERE Student_Id={id}")
                roll = cursor.fetchone()
                roll = "+".join(roll) if roll else "Unknown"
                
                cursor.execute(f"SELECT Department FROM student WHERE Student_Id={id}")
                dep = cursor.fetchone()
                dep = "+".join(dep) if dep else "Unknown"
                
                if confidence > 77:
                    cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    
                coord = [x, y, w, h]
                
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to break the loop
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
