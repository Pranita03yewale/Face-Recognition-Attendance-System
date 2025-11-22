from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import mysql.connector

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\train1.jpeg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        btn1 = Button(self.root, text="TRAIN DATA", width=36, font=("times new roman", 30, "bold"), bg="red", fg="white", command=self.train_classifier)
        btn1.place(x=0, y=380, width=1530, height=60)

        img_bottum = Image.open(r"images\train2.jpeg")
        img_bottum = img_bottum.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottum = ImageTk.PhotoImage(img_bottum)

        f_lbl = Label(self.root, image=self.photoimg_bottum)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ========= Train the classifier and save ===============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
