from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import tkinter
import mysql.connector
# --------------------------
from train import Train
from report import report
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from Speak import Speak



class Face_Recognition_Software:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("680x530+0+0")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)

        # variables 
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()

        
        
        bg1=Image.open(r"Images\1_FOT7m7RYX4bLcEBGthowkQ.png")
        bg1=bg1.resize((680,530),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=680,height=530)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=0,y=0,width=680,height=530)

        img1=Image.open(r"Images\sindh.png")
        img1=img1.resize((120,120),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=0,y=0, width=120,height=120)
        
        img2=Image.open(r"Images\imcs.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Label(image=self.photoimage2,bg="#002B53")
        lb1img2.place(x=575,y=5, width=100,height=100)

        get_str = Label(frame1,text="Login ",font=("Goudy Old Style",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=290,y=230)
        
        uni = Label(frame1,text="University Of Sindh,Jamshoro",font=("Goudy Old Style",25,"bold"),fg="white",bg="#002B53")
        uni.place(x=130,y=40)
        
        uni = Label(frame1,text="Institute of Mathamatics and Computer Science",font=("Goudy Old Style",23,"bold"),fg="white",bg="#002B53")
        uni.place(x=40,y=130)
        
        uni = Label(frame1,text="Face Recognition Attendence System",font=("Goudy Old Style",25,"bold"),fg="white",bg="#002B53")
        uni.place(x=80,y=170)
        
        #label1 
        username =lb1= Label(frame1,text="Email:",font=("Goudy Old Style",15,""),fg="white",bg="#002B53")
        username.place(x=50,y=270)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("Goudy Old Style",15,""))
        self.txtuser.place(x=50,y=300,width=570)


        #label2 
        password =lb1= Label(frame1,text="Password:",font=("Goudy Old Style",15,"bold"),fg="white",bg="#002B53")
        password.place(x=50,y=330)

        #entry2 
        self.txtpassword=ttk.Entry(frame1,font=("Goudy Old Style",15,"bold"),show="*")
        self.txtpassword.place(x=50,y=360,width=570)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("Goudy Old Style",22,"bold"),bd=0,relief=RIDGE,fg="white",bg="#007ACC",activeforeground="#007ACC",activebackground="white")
        loginbtn.place(x=50,y=420,width=570,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("Goudy Old Style",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=50,y=500,width=50,height=20)
        
         # Creating Button Student
        loginbtn=Button(frame1,command=self.student_pannels,text=" If You are Student Fill Form Here? ",width=20,font=("Goudy Old Style",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=355,y=500,width=300,height=25)

        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_password,text="Forget",font=("Goudy Old Style",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=120,y=500,width=50,height=20)

     #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def face_R(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_Software(self.new_window)

    def close_window(self):
        #self.var_question.set("Selete")
        self.txtuser.delete(0,END)
        self.txtpassword.delete(0,END)
        #self.var_answer.delete(0,END)
        #self.new_password.delete(0,END)

    def login(self):
        if (self.txtuser.get()==""):
            #messagebox.showerror("Error","Please Enter the Email!",parent=self.root)
            Speak("Please Enter the Email")
        elif(self.txtpassword.get()==""):
            #messagebox.showerror("Error","Please Enter the Password!",parent=self.root)
            Speak("Please Enter the Password")
        elif(self.txtuser.get()=="admin" and self.txtpassword.get()=="admin"):
            #messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System",parent=self.root)
            Speak("Welcome to Face Recognition Attendance Managment System")
        else:
            try:
                # messagebox.showerror("Error","Please Check Username or Password !")
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from register where email=%s and password=%s",(
                    self.txtuser.get(),
                    self.txtpassword.get()
                ))
                row=mycursor.fetchone()
                if row==None:
                    #messagebox.showerror("Error","Invalid Email and Password!",parent=self.root)
                    Speak("Invalid Email and Password")
                else:
                    open_min=messagebox.askyesno("YesNo","Access only Teacher")
                    #messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System",parent=self.root)
                    Speak("Welcome to Face Recognition Attendance Managment System")
                    if open_min>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_min:
                        
                            return
                conn.commit()

                conn.close()
            except Exception as es:
                Speak("Please Check the Notification and Read Carefuly")
                messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root)
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_question.get()=="Select":
            Speak("Please Select the Security Question")
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
            
        elif(self.var_answer.get()==""):
            Speak("Please Enter the Answer")
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
            
        elif(self.var_password.get()==""):
            Speak("Please Enter the New Password")
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s and question=%s and answer=%s")
                value=(self.txtuser.get(),self.var_question.get(),self.var_answer.get())
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Verify Correct Question & Answer!",parent=self.root2)
                    Speak("Don't Worry Try Again")
                    messagebox.showerror("Error","Don't Worry Try Again...!!",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.var_password.get(),self.txtuser.get())
                    mycursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    Speak("Reset Password Process has been Successfully  Please login with new a Password")  
                    messagebox.showinfo("Info","Process has been Successfully....! \nYour Password Has Been Reset....!\nlogin with new Password!",parent=self.root2)
                    self.close_window()
                    self.root2.destroy()
                    self.face_R()
            except Exception as es:
                 messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root2)       
                  
# =====================Forget window=========================================
    def forget_password(self):
        if self.txtuser.get()=="":
            Speak("Please Enter the Email Address to Reset Password")
            messagebox.showerror("Error","Please Enter the Email Address to Forget Password!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                # print(row)

                if row==None:
                    Speak("Please Enter the Valid Email Address")
                    messagebox.showerror("Error","Please Enter the Valid Email Address!",parent=self.root)
                else:
                    Speak("Forget Password Process Started")
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+610+170")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                    l.place(x=0,y=10,relwidth=1)
                    # -------------------fields-------------------
                    #label1 
                    question =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    question.place(x=70,y=80)

                    #Combo Box1
                    self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_question,font=("times new roman",12,"bold"),state="readonly")
                    self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                    self.combo_security.current(0)
                    self.combo_security.place(x=70,y=110,width=270)

                

                    #label2 
                    answer =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    answer.place(x=70,y=150)

                    #entry2 
                    self.txtpassword=ttk.Entry(self.root2,textvariable=self.var_answer,font=("times new roman",12,"bold"))
                    self.txtpassword.place(x=70,y=180,width=270)

                    #label2 
                    new_password =lb1= Label(self.root2,text="New Password:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    new_password.place(x=70,y=220)

                    #entry2 
                    self.new_password=ttk.Entry(self.root2,textvariable=self.var_password,font=("times new roman",12,"bold"),show="*")
                    self.new_password.place(x=70,y=250,width=270)

                    #checkPassword
                    checkbtn = Checkbutton(self.root2,textvariable=self.var_password,font=("Goudy Old Style",11,"bold"),fg="#002B53",bg="#F2F2F2")
                    checkbtn.place(x=70,y=280,width=270)


                    # Creating Button New Password
                    loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",12,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                    loginbtn.place(x=70,y=310,width=270,height=35)

                    #Button BACK
                    #backbutton=Button(self.root2.destroy,text="Back",font=("times new roman",12,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                    #backbutton.place(x=70,y=330,width=270,height=25) 
            except Exception as es:
                 messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root)
               

# =====================main program Face deteion system====================

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Face_Recogonition_System")
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

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
       

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="DATA TRAIN",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        tra_b1_1.place(x=110,y=340,width=120,height=30)

        # Photo   button 6
       

        #pho_b1_1 = Button(bg_img,command=self.open_img,text="IMAGE SAMPLE",cursor="hand2",font=("tahoma",9,"bold"),bg="darkgreen",fg="white")
        #pho_b1_1.place(x=400,y=260,width=120,height=30)

        # Developers   button 7
        

        dev_b1_1 = Button(bg_img,command=self.developr,text="DEVELOPERS",cursor="hand2",bd=0,font=("tahoma",9,"bold"),bg="navyblue",fg="white")
        dev_b1_1.place(x=180,y=393,width=120,height=30)
        
        # exit   button 
        
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
        #self.new_window=Toplevel(self.root)
        #self.app=Helpsupport(self.new_window)

    def iExit(self):
        Speak('Are You Sure To Leave Application')
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure To Leave Application",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    
if __name__ == "__main__":
    root=Tk()
    app=Face_Recognition_Software(root)
    root.mainloop()