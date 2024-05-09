import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\lenovo\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="faceicon.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Attendence Management System Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["faceicon.ico","tcl86t.dll","tk86t.dll","Images","data_img","databaseTest","Attendence_Data"]}},
    version = "2.0",
    description = "Face Recognition Automatic Attendace System | Developed By MUHAMMAD SAJAN KALHORO",
    executables = executables
    )
