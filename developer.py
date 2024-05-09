from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Face_Recognition_System")
        self.root.wm_iconbitmap("faceicon.ico")


        # backgorund image 
        # Creating Frame 
        main_frame = Frame(self.root,bd=2,bg="black") #bd mean border 
        main_frame.place(x=0,y=20,width=680,height=510)



        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="DEVELOPERS",font=("verdana",12,"bold"),fg="white")
        left_frame.place(x=0,y=20,width=665,height=488)


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
        # student button_1
        det_img_btn=Image.open(r"Images\uzair.jpg")
        det_img_btn=det_img_btn.resize((130,150),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)
        
        det_b1 = Label(left_frame,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=10,y=30,width=130,height=150)
        
        det_b1_1 = Label(left_frame,text='Project Manager',cursor="hand2",bd=0,font=("tahoma",9,""),bg="black",fg="white")
        det_b1_1.place(x=10,y=210,width=130,height=30)

        det_b1_1 = Label(left_frame,text="MUHAMMAD UZAIR",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="navyblue",fg="white")
        det_b1_1.place(x=10,y=260,width=130,height=30)
        
        # Student 2
        det_img=Image.open(r"Images\memon.jpg")
        det_img=det_img.resize((130,150),Image.ANTIALIAS)
        self.det_img=ImageTk.PhotoImage(det_img)
        
        det_b2 = Label(left_frame,image=self.det_img,cursor="hand2",)
        det_b2.place(x=170,y=30,width=130,height=150)
        
        det_b1_2 = Label(left_frame,text='Python Developer',cursor="hand2",bd=0,font=("tahoma",9,""),bg="black",fg="white")
        det_b1_2.place(x=170,y=210,width=130,height=30)

        det_b1_2 = Label(left_frame,text="JAWAD MEMON",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="navyblue",fg="white")
        det_b1_2.place(x=170,y=260,width=130,height=30)
        
        #Student 3
        
        det_img3=Image.open(r"Images\adeel.jpeg")
        det_img3=det_img3.resize((130,150),Image.ANTIALIAS)
        self.det_img3=ImageTk.PhotoImage(det_img3)
        
        det_b3 = Label(left_frame,image=self.det_img3,cursor="hand2",)
        det_b3.place(x=330,y=30,width=130,height=150)
        
        det_b1_3 = Label(left_frame,text='Thesis',cursor="hand2",bd=0,font=("tahoma",10,""),bg="black",fg="white")
        det_b1_3.place(x=330,y=210,width=130,height=30)

        det_b1_3 = Label(left_frame,text="ADEEL KHERO",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="navyblue",fg="white")
        det_b1_3.place(x=330,y=260,width=130,height=30)
        
        #Studen 4
        
        det_img4=Image.open(r"Images\raza.jpeg")
        det_img4=det_img4.resize((130,150),Image.ANTIALIAS)
        self.det_img4=ImageTk.PhotoImage(det_img4)
        
        det_b4 = Label(left_frame,image=self.det_img4,cursor="hand2",)
        det_b4.place(x=500,y=30,width=130,height=150)
        
        det_b1_4 = Label(left_frame,text='Thesis',cursor="hand2",bd=0,font=("tahoma",10,""),bg="black",fg="white")
        det_b1_4.place(x=490,y=210,width=130,height=30)

        det_b1_4 = Label(left_frame,text="ALI RAZA JATOI",cursor="hand2",bd=0,font=("tahoma",10,"bold"),bg="navyblue",fg="white")
        det_b1_4.place(x=500,y=260,width=130,height=30)

        # Attendance System  button 3
    #def LinkedIn(self):
       # self.new = 1
        #self.url = "https://www.linkedin.com/in/M-Sajan-Kalhoro7246"
        #webbrowser.open(self.url,new=self.new)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()