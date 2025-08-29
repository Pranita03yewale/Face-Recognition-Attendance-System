from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  # For capturing images
import os 
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #==================variables===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        
        
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
        
        # background image
        img3 = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\bg6.jpg")
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
 
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        
        # left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\student.jpg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
 
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)
        
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=750,height=115)
        
        #department
        
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FY","SY","TY","BTECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        #year
        
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem I","Sem II","Sem III","Sem IV")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class student information
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=17,y=280,width=750,height=304)
        
        # student id
        
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
         # student name
        
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
         #class division
        
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        division_combo["values"]=("Select ","A","B","c","D","Other")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
         #Roll No
        
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
         #Gender
        
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select ","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
         #DOB
        
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_label_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_label_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
         #Email
        
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_label_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_label_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
         #Mobile No
        
        mobile_label=Label(class_student_frame,text="Mobile No:",font=("times new roman",13,"bold"),bg="white")
        mobile_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        mobile_label_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_mobile,font=("times new roman",13,"bold"))
        mobile_label_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
         #Address
        
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_label_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_label_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
         #Teacher name
        
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_label_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_label_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value=":Yes")
        radiobtn1.grid(row=6,column=0)
        
    
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #buttons frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=205,width=740,height=35)
        
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=240,width=740,height=35)
        
        take_photo_btn1 = Button(btn_frame1, text="Take Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.take_photo_sample)
        take_photo_btn1.grid(row=1, column=0)

        update_btn1 = Button(btn_frame1, text="Update Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=lambda: (self.update_photo_sample(), self.update_photo_sample_status()))
        update_btn1.grid(row=1, column=1)

    
        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=580)
        
        img_right = Image.open(r"C:\Users\admin\Desktop\face recognition attendance system\images\frsimg.jpg")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
 
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=750, height=130)
        
        # =========search system==========
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Roll_No","Mobile_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=13,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        #===============table frame==============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","mobile","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("mobile",text="Mobile")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("mobile",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=200)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root@123",database="face_recognition_attendance_system")
                my_cursor=conn.cursor()
                query = "INSERT INTO student (department, course, year, semester, student_id, student_name, division, roll, gender, dob, email, mobile, address, teacher, PhotoSampleStatus, photo_sample_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_mobile.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), 'Pending')
                my_cursor.execute(query, values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root@123",database="face_recognition_attendance_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_mobile.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root@123",database="face_recognition_attendance_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Mobile=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_Id=%s",(
                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                            self.var_course.get(),
                                                                                                                                                            self.var_year.get(),
                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                            self.var_div.get(),
                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root@123",database="face_recognition_attendance_system")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobile.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    
    #==========================Generate data set or Take photo sample===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root@123",database="face_recognition_attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Mobile=%s,Address=%s,Teacher=%s where Student_Id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                    
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.1,4)
                    #scaling factor=1.1
                    #Minimum Neighbors=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #==========================Function Buttons========================================
    
    def take_photo_sample(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_radio1.get() == "":
            messagebox.showerror("Error", "Photo sample is required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root@123",
                    database="face_recognition_attendance_system"
                )
                my_cursor = conn.cursor()

                # Fetch the specific student ID
                student_id = self.var_std_id.get()
                my_cursor.execute("SELECT * FROM student WHERE Student_Id=%s", (student_id,))
                myresult = my_cursor.fetchall()

                # Update student record in the database if exists
                if myresult:
                    my_cursor.execute(
                        "UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Student_name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Mobile=%s, Address=%s, Teacher=%s WHERE Student_Id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_mobile.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            student_id
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load predefined data on face frontals from opencv
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.1, 4)
                        # Scaling factor=1.1
                        # Minimum Neighbors=4
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set completed!!!")
                else:
                    messagebox.showerror("Error", "Student ID not found", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        def update_photo_sample(self):
            if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif self.var_radio1.get() == "":
                messagebox.showerror("Error", "Photo sample is required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Mobile=%s,Address=%s,Teacher=%s where Student_Id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_mobile.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_std_id.get() == id + 1
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load predefined data on face frontals from OpenCV
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.1, 4)
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set completed!!!")
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def update_photo_sample_status(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="face_recognition_attendance_system")
            my_cursor = conn.cursor()
            update_query = "UPDATE student SET photo_sample_status = %s WHERE Student_Id = %s"
            values = ("Updated", self.var_std_id.get())
            my_cursor.execute(update_query, values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Photo sample status updated successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
