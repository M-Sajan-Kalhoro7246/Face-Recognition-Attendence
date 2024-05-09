# import re
import re
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
class AttendenceReport:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Attendance Panel")
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

        #title section
        title_lb1 = Label(self.root,text=" IMCS  Face Recognition Attendence System",font=("verdana",15,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=666,height=35)
        
        
        img2=Image.open(r"Images\update.png")
        img2=img2.resize((50,35),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Button(title_lb1,command=root.destroy,image=self.photoimage2,bd=0,bg="black")
        lb1img2.place(x=610,y=0, width=50,height=35)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(self.root,bd=2,bg="black") #bd mean border 
        main_frame.place(x=0,y=35,width=666,height=520)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="white")
        left_frame.place(x=0,y=10,width=663,height=473)


        # Right section======================================================= 

        


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(left_frame,bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=10,y=10,width=640,height=400)

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
        del_btn=Button(left_frame,command=self.delete_data,text="Delete",bd=0,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)
        del_btn.place(x=250,y=415, width=150,height=30)
    # ===============================update function for mysql database=================
    def update_data(self):                                                              # or self.var_dep.get()==""
        if self.var_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
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
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=AttendenceReport(root)
    root.mainloop()