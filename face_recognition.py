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
import pyttsx3
#========= functions =============
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Face Recognition Pannel")
        self.root.wm_iconbitmap("faceicon.ico")

        

        # backgorund image 
        bg1=Image.open(r"Images\images (10).jpeg")
        bg1=bg1.resize((666,520),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=666,height=520)
        
        #title section
        title_lb1 = Label(self.root,text=" IMCS  Face Recognition Attendence System",font=("verdana",15,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=680,height=35)

        
        img2=Image.open(r"Images\update.png")
        img2=img2.resize((50,35),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lb1img2 = Button(title_lb1,command=root.destroy,image=self.photoimage2,bd=0,bg="black")
        lb1img2.place(x=610,y=0, width=50,height=35)


        #Note Message Button1
        Note_lb1 = Label(bg_img,text="Press Enter Button to Destroy Camera Section->",font=("verdana",10,"bold"),bg="black",fg="white")
        Note_lb1.place(x=0,y=520,width=680,height=25)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 

        img3=Image.open(r"Images\images (16).jpeg")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lb1img2 = Button(bg_img,command=self.face_recog,image=self.photoimage3,bd=0,bg="black")
        lb1img2.place(x=400,y=200, width=200,height=200)
        
        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",bd=0,font=("verdana",13,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=400,y=420,width=200,height=35)

        #Note Message Button1
        Note_lb1 = Label(bg_img,text="Press Enter Button to Destroy Camera Section ->",font=("verdana",10,"bold"),bg="darkred",fg="white")
        Note_lb1.place(x=5,y=495,width=390,height=20)
    
    #=====================Attendance===================

    def mark_attendance(self,Student_ID,Roll_No,Name):
        with open(r"Attendence_Data\Attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))

                name_list.append(entry[0])

            if((Student_ID not in name_list)) and ((Roll_No not in name_list)) and ((Name not in name_list)):
                now=datetime.now()
                d1=now.strftime("%Y/%m/%d")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{Student_ID}, {Roll_No}, {Name}, {dtString}, {d1}, Present")




    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                Name=cursor.fetchone()
                Name="+".join(Name)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                Roll_No=cursor.fetchone()
                Roll_No="+".join(Roll_No)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                Student_ID=cursor.fetchone()
                Student_ID="+".join(Student_ID)
                    

                if confidence > 77:
                    #Speak(f"Student ID {Student_ID} Attendence Successfuly")
                    cv2.putText(img,f"Student_ID:{Student_ID}",(x,y-88),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{Name}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll_No:{Roll_No}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    #cv2.putText(img,f"Department:{Department}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(Student_ID,Name,Roll_No)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    
                    #Speak("Unknown Face"),
                coord=[x,y,w,y]
            
            return coord    



        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)
        address ="http://192.168.0.103:8080/video"
        videoCap.open(address)
        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)
            
            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        
        cv2.destroyAllWindows()

#================ FUNCTION ==================
"""
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',170)
    print("")
    print(f"Ai : {Text}. ")
    print("")
    engine.say(Text)
    engine.runAndWait()
"""

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()