from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
#from helpsupport import Helpsupport
from report import report
#=========================================



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Face_Recognition_System")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)

        # backgorund image 
        bg1=Image.open(r"Images\main.jpg")
        bg1=bg1.resize((800,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=800,height=520)
        
        title_lb1 = Label(self.root,text=" IMCS  Face Recognition Attendence System",font=("verdana",15,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=666,height=30)

        # Detect Face  button 2        
                     
        det_b1_1 = Button(bg_img,command=self.face_rec,text="FACE DETECTOR",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        det_b1_1.place(x=35,y=280,width=120,height=30)

         # Attendance System  button 3

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="ATTENDANCE",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        att_b1_1.place(x=180,y=280,width=120,height=30)

         # Report  button 4

        hlp_b1_1 = Button(bg_img,command=self.report,text="ADMIN PANEL",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        hlp_b1_1.place(x=35,y=393,width=120,height=30)

         # Train   button 5
         
        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="DATA TRAIN",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        tra_b1_1.place(x=110,y=340,width=120,height=30)     

        #pho_b1_1 = Button(bg_img,command=self.open_img,text="IMAGE SAMPLE",cursor="hand2",font=("tahoma",9,"bold"),bg="darkgreen",fg="white")
        #pho_b1_1.place(x=400,y=260,width=120,height=30)

        # Developers   button 7
    
        dev_b1_1 = Button(bg_img,command=self.developr,text="DEVELOPERS",cursor="hand2",bd=0,font=("tahoma",9,"bold") ,bg="#80669d",fg="white")
        dev_b1_1.place(x=180,y=393,width=120,height=30)
        # exit   button 8
        img2=Image.open(r"Images\exit3.png")
        img2=img2.resize((50,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Button(bg_img,command=self.iExit,image=self.photoimage2,bd=0,bg="#0a0a0a")
        lb1img2.place(x=600,y=450, width=50,height=50)
       
        
# ==================Funtion for Open Images Folder ==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)
    
    #def helpSupport(self):
       # self.new_window=Toplevel(self.root)
       # self.app=Helpsupport(self.new_window)

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure To Exit This Project",parent=self.root)
         if self.iExit>0:
             self.root.destroy()
         else:
                 return
    
    


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
