from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from Speak import Speak

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Train Pannel")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)


        # backgorund image 
        bg1=Image.open(r"Images\Train_bg.png")
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

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="TRAIN DATASET",cursor="hand2",bd=0,font=("tahoma",12,""),bg="blue",fg="white")
        std_b1_1.place(x=250,y=470,width=160,height=40)

        #button back
    

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier and save =============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        Speak('Training Dataset Completed')
        messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)

    
    


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()