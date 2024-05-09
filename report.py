from tkinter import *
from tkinter import ttk
import tkinter  as tk 
from PIL import Image,ImageTk
import mysql.connector

import os
from RReport import Register_Report
from AReport import AttendenceReport
from SReport import StudentReport
class report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Face Recogonition System")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)

        # backgorund image 
        bg1=Image.open(r"Images\adminp.jpg")
        bg1=bg1.resize((666,520))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=10,width=666,height=510)


        #title section
        title_lb1 = Label(self.root,text=" IMCS  Face Recognition Attendence System",font=("verdana",15,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=680,height=35)
        
        img2=Image.open(r"Images\update.png")
        img2=img2.resize((50,35),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Button(title_lb1,command=root.destroy,image=self.photoimage2,bd=0,bg="black")
        lb1img2.place(x=610,y=0, width=50,height=35)
        
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        det_img_btn=Image.open(r"Images\admin2.png")
        det_img_btn=det_img_btn.resize((200,150))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Label(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=52,y=170,width=200,height=150)

        det_b1_1 = Button(bg_img,command=self.AttendenceReport,text="Attendance",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="blue",fg="white")
        det_b1_1.place(x=180,y=340,width=150,height=30)

        # student button 2  

        det_b2_2 = Button(bg_img,command=self.StudentReport,text="Student",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="blue",fg="white")
        det_b2_2.place(x=10,y=340,width=150,height=30)

        # student button 3
        det_b3_3 = Button(bg_img,command=self.RegisterReport, text="Registered",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="blue",fg="white")
        det_b3_3.place(x=90,y=390,width=150,height=30)
      # Attendance System  button 3
    def RegisterReport(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Report(self.new_window)
        
    def AttendenceReport(self):
        self.new_window=Toplevel(self.root)
        self.app=AttendenceReport(self.new_window)
        
    def StudentReport(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentReport(self.new_window)  

    
if __name__ == "__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()