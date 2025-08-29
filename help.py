from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\help1.webp")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        dev_label1 = Label(f_lbl, text="Email : attendancehelp@gmail.com", font=("times new roman", 20, "bold") )
        dev_label1.place(x=590, y=350)
        dev_label1 = Label(f_lbl, text="Contact No. : 9876543112", font=("times new roman", 20, "bold"))
        dev_label1.place(x=590, y=400)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
