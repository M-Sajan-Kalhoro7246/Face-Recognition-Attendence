# import re
import re
from Speak import Speak
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
import pandas as pd

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Attendance Pannel")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        #self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # backgorund theme
        
        bg_img = Frame(self.root,bd=2,bg="black") 
        bg_img.place(x=0,y=20,width=666,height=520)

        title_lb1 = Label(self.root,text=" IMCS  Face Recognition Attendence System",font=("verdana",15,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=666,height=35)
        #button back
        img2=Image.open(r"Images\update.png")
        img2=img2.resize((50,35),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Button(title_lb1,command=root.destroy,image=self.photoimage2,bd=0,bg="black")
        lb1img2.place(x=610,y=0, width=50,height=35)
        
        #tra_b1_1 = Button(title_lb1,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        #tra_b1_1.place(x=620,y=10,width=150,height=30)
        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="black") #bd mean border 
        main_frame.place(x=0,y=10,width=666,height=510)

        #Left Label Frame 
        #left_frame = LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="white")
        #left_frame.place(x=10,y=10,width=660,height=480)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(main_frame,text="ID:",font=("verdana",12,"bold"),fg="white",bg="black")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(main_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Name
        student_name_label = Label(main_frame,text="Name",font=("verdana",12,"bold"),fg="white",bg="black")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(main_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Roll.No
        student_roll_label = Label(main_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="white",bg="black")
        student_roll_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(main_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Department
        #dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        #dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        #dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        #dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(main_frame,text="Time:",font=("verdana",12,"bold"),fg="white",bg="black")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(main_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(main_frame,text="Date:",font=("verdana",12,"bold"),fg="white",bg="black")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(main_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(main_frame,text="Attendence:",font=("verdana",12,"bold"),fg="white",bg="black")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(main_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        table_frame = Frame(main_frame,bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=10,y=140,width=635,height=300)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Name","Roll_No","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="ID")
        self.attendanceReport_left.heading("Name",text="Name")
        self.attendanceReport_left.heading("Roll_No",text="Roll.No")
        #self.attendanceReport_left.heading("dep",text="Department")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend-status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Roll_No",width=100)
        #self.attendanceReport_left.column("dep",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(main_frame,bd=0,bg="black",relief=RIDGE)
        btn_frame.place(x=10,y=440,width=635,height=50)

        #Improt button
        
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=13,bd=0,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,command=self.CleanData,text="Clean Data",width=13,bd=0,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Update",width=12,bd=0,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,bd=0,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)

        

        # Right section======================================================= 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Name","Roll_No","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="ID")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        #self.attendanceReport.heading("dep",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        #self.attendanceReport.column("dep",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================
    #Update button
        del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Update button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
    # ===============================update function for mysql database=================
    def update_data(self):                                                              # or self.var_dep.get()==""
        if self.var_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            Speak("Please Fill All Fields are Required!")
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_name=%s,std_roll_no=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    #self.var_dep.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
         
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")  
        self.var_name.set("")
        self.var_roll.set("")
        #self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            #print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Experot CSV=============
    def CleanData(self):
        f = open('Attendence_Data\\Attendance.csv',"w+")
        f.close()
       


    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]
        #print(data)
        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),     
        #self.var_dep.set(data[3]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),   
        #self.var_dep.set(data[3]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])   
    #=========================================Update CSV============================   

    # export upadte                                                                     # or self.var_dep.get()==""
    def action(self):
        if self.var_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_name.get(),
                self.var_roll.get(),
                #self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                Speak("All Records are Saved in Database")
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()