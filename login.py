from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import tkinter
import mysql.connector
from student import Student
from help import Help
from developer import Developer
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #self.bg = ImageTk.PhotoImage(file=r"C:\Users\admin\Desktop\face recognition attendance system\images\login.jpeg")
        #lbl_bg = Label(self.root, image=self.bg)
        #lbl_bg.place(x=0, y=0, relwidth=1,relheight=1)

        # background image
        img3 = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\bgimg 3.jpg")
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
 
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #========= Project button (description)========
        downtitle=Label(self.root,text="Notr:Enter valid username and valid password",font=("times new roman",15,"bold"),bg="white",fg="red")
        downtitle.place(x=0,y=740,width=1600,height=35)

        # first image
        img = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\middleimg.jpg")
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        # second image
        img1 = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\frsimg.jpg")
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
        # third image
        img2 = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\firstimg.webp")
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
 
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)
        

        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=210,width=340,height=450)

        img1=Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\login logo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=195,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label 1
        username=Label(frame,text='Username',font=("times new roman",15,'bold'),fg='white',bg='black')
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=('time new roman',15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text='Password',font=("times new roman",15,'bold'),fg='white',bg='black')
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=('time new roman',15,"bold"), show='*')
        self.txtpass.place(x=40,y=250,width=270)

         #======= Icon image ======
        img2=Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\login logo.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=365,width=25,height=25)

        img3=Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\pass.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=430,width=25,height=25)

        # Login button
        loginbtn = Button(frame, text="Login",command=self.login_data, borderwidth=3, relief=RAISED,  cursor="hand2", font=("times new roman", 15, "bold"), bd=3, fg="white", bg="red", activebackground="white", activeforeground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn=Button(frame,text="New User Registration",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="red")
        registerbtn.place(x=30,y=350,width=170)

        # Forget Password button
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="red")
        registerbtn.place(x=30,y=380,width=140)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login_data(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
        
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                
            conn.commit()
            conn.close()

   #==================== reset password ========================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and security_question=%s and security_answer=%s" )
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())  # Added .get()
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct Answer", parent=self.root2)
            else:
                # Close the previous cursor and connection
                my_cursor.close()
                conn.close()

                # Reconnect to execute the update query
                conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
                my_cursor = conn.cursor()
                
                query = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset. Please log in with your new password", parent=self.root2)
                self.root2.destroy()


    #================== forgot password window ================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter the Email address to reset the password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)

            if row== None:
                messagebox.showerror("My Error", "Plaese enter the valid user name")

            else:
                conn.close()
                self.root2 =Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

            l=Label(self.root2, text=" Forget Password", font=("times new roman", 30, "bold"), fg="red",bg="white") 
            l.place(x=0,y=10, relwidth=1)

            security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_Q.place(x=50, y=80)
            self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15))
            self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name","Your Nick Name","Your favourite dish")
            self.combo_security_Q.place(x=50, y=110, width=250)

            security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_A.place(x=50, y=150)
            self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_security.place(x=50, y=180, width=250)

            new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
            new_password.place(x=50, y=220)
            self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_newpass.place(x=50, y=250, width=250)

            btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15),fg="white",bg="green")
            btn.place(x=120,y=290)

            
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==== variables ======
        self.var_fname = StringVar()
        self.var_l_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_Q = StringVar()
        self.var_security_A = StringVar()
        self.var_pswd = StringVar()
        self.var_confirm_pswd = StringVar()

        # Bg Image
        self.bg = ImageTk.PhotoImage(file="images/login.jpeg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        self.bg1 = ImageTk.PhotoImage(file="images/rg2.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Register Label
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Label and Entry
        #====== Row 1 ==============
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)
        self.txt_l_name = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_l_name.place(x=370, y=130, width=250)

        #====== Row 2 ==============
        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        #======= Row 3 ================
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15))
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name","Your Nick Name","Your favourite dish")
        self.combo_security_Q.place(x=50, y=270, width=250)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #========= Row 4============
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txr_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txr_confirm_pswd.place(x=370, y=340, width=250)

        #======== check button ========
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, text="I Agree the Terms & Conditions", font=("times new roman", 15, "bold"), variable=self.var_check)
        checkbtn.place(x=50, y=380)

        #========== button ==========
        # Image 1 Button
        register_btn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="red", fg="white", relief=FLAT, borderwidth=2, highlightthickness=0)
        register_btn.place(x=300, y=420, width=180, height=40)
        register_btn.config(border=5)

        login_btn = Button(frame, text="Login", command=self.return_login, font=("times new roman", 15, "bold"), bg="blue", fg="white", relief=FLAT, borderwidth=2, highlightthickness=0)
        login_btn.place(x=500, y=420, width=180, height=40)
        login_btn.config(border=5)  # Add this line to create a round border

    #==== function declaration ==========
    def register_data(self):
        if self.fname_entry.get() == "" or self.txt_email.get() == "" or self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.txt_pswd.get() != self.txr_confirm_pswd.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our Terms and Conditions")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root@123",
                    database="face_recognition_attendance_system"
                )
                cursor = conn.cursor()

                # Check if email already exists
                query = "SELECT * FROM register WHERE email = %s"
                cursor.execute(query, (self.txt_email.get(),))
                row = cursor.fetchone()
                
                if row:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    insert_query = "INSERT INTO register (first_name, last_name, contact_no, email, security_question, security_answer, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    data = (
                        self.fname_entry.get(),
                        self.txt_l_name.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.combo_security_Q.get(),
                        self.txt_security.get(),
                        self.txt_pswd.get()
                    )
                    cursor.execute(insert_query, data)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def return_login(self):
        self.root.destroy()
        # Define the login functionality
        pass


        
    #====================function================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def help_details(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)


    def login(self):
        # Define the login functionality
        pass

    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
          
        


if __name__ == "__main__":
    main()

