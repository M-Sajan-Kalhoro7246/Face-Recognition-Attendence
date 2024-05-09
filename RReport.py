from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

from tkcalendar import Calendar,DateEntry
import mysql.connector
import cv2
# Testing Connection 
"""
conn = mysql.connector.connect(usern='root', password='',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Register_Report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("666x520+0+0")
        self.root.title("Registered Report")
        self.root.wm_iconbitmap("faceicon.ico")
        self.root.resizable(False, False)

        #-----------Variables-------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        self.var_check=IntVar()

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
        
        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Registered Details",font=("verdana",12,"bold"),fg="white")
        right_frame.place(x=0,y=10,width=665,height=473)

        #Delete Button
        Delete_Button=Button(right_frame,command=self.delete_data,text="Delete",bd=0,font=("verdana",12,"bold"),bg="navyblue",fg="white")
        Delete_Button.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        Delete_Button.place(x=240,y=415, width=150,height=30)
        
        #button back

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=10,y=50,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=('fname','lname','contact','email','question','answer','password'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("fname",text="First Name")
        self.student_table.heading("lname",text="Last Name")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("question",text="Question")
        self.student_table.heading("answer",text="Answer")
        self.student_table.heading("password",text="Password")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("fname",width=100)
        self.student_table.column("lname",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("question",width=100)
        self.student_table.column("answer",width=100)
        self.student_table.column("password",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    
            


    # ===========================Fetch data form database to table ================================

    def fetch_data(self):


        conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from register")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_fname.set(data[0]),
        self.var_lname.set(data[1]),
        self.var_contact.set(data[2]),
        self.var_email.set(data[3]),
        self.var_question.set(data[4]),
        self.var_answer.set(data[5]),
        self.var_password.set(data[6]),
        self.var_cpassword.set(data[7]),
    # ========================================Update Function==========================
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_email.get()=="":
            messagebox.showerror("Error","Teacher Email Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from register where email=%s"
                    val=(self.var_email.get(),)
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

    
# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Register_Report(root)
    root.mainloop()
