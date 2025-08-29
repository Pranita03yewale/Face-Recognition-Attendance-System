from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\dev.webp")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  # Updated here
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        #======= frame 1 =======
        main_frame1 = Frame(f_lbl, bd=2, bg="white")
        main_frame1.place(x=500, y=200, width=500, height=300)

        # Developer 1
        img_top1 = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\pranita.jpg")
        img_top1 = img_top1.resize((250, 250), Image.Resampling.LANCZOS)  # Updated here
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame1, image=self.photoimg_top1)
        f_lbl1.place(x=200, y=0, width=280, height=280)

        dev_label1 = Label(main_frame1, text="Pranita Prabhakar Yewale", font=("times new roman", 13, "bold"), bg="white")
        dev_label1.place(x=0, y=5)
        dev_label1 = Label(main_frame1, text="Class : T.Y. CSE ,    Div : B", font=("times new roman", 13, "bold"), bg="white")
        dev_label1.place(x=0, y=40)
        dev_label1 = Label(main_frame1, text="Roll No. : 134 ", font=("times new roman", 13, "bold"), bg="white")
        dev_label1.place(x=0, y=75)
        dev_label1 = Label(main_frame1, text="PRN No. : 2162701242107", font=("times new roman", 13, "bold"), bg="white")
        dev_label1.place(x=0, y=110)

         

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
