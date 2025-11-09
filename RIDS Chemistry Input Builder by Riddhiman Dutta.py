from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog

#LabelFrame(root,width=100, height=350,bd=2).place(x=500,y=350),LabelFrame(root,width=100, height=350,bd=2).place(x=500,y=350)


root=Tk()
root.geometry("1070x550")
root.resizable(0,0)


#Functions
def open_file():
       file_path = filedialog.askopenfilename(
           title="Select a text file",
           filetypes=[("Text files", "*.xyz"), ("All files", "*.*")]
       )
       if file_path:
           try:
               with open(file_path, 'r', encoding='utf-8') as file:
                   line1=file.readline()
                   molno=int(line1)
                   Label(outframe, text=f"Number of atoms={molno}").place(x=915,y=70)

                   line2=file.readline()
                   content = file.readlines()
                   content_str = "".join(content)
                   Label(outframe, text=content_str).place(x=915,y=90)
                   
           except Exception as e:
               text_area.delete(1.0, tk.END)
               text_area.insert(tk.END, f"Error reading file: {e}")





def save_file():
    global rtype,scf,mcharge,mul,max
    max=omax.get()
    mul=omul.get()
    mcharge=omcharge.get()
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
           # Get all text from the Text widget
           tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={rtype.get()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
           tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
           tex3=Label(outframe,text=f" $BASIS GBASIS=MINI $END")
           tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
           tex5=Label(outframe,text=f" $DATA")
           tex6=Label(outframe,text=f"Title")
           tex7=Label(outframe,text=f"C1")
        

           txt1=tex1.cget("text")
           txt2=tex2.cget("text")
           txt3=tex3.cget("text")
           txt4=tex4.cget("text")
           txt5=tex5.cget("text")
           txt6=tex6.cget("text")
           txt7=tex7.cget("text")

           # Write the content to the selected file
           with open(file_path, "w") as file:
              file.write(txt1+"\n")
           with open(file_path, "a") as file:
            file.write(txt2+"\n")
           with open(file_path, "a") as file:
            file.write(txt3+"\n")
           with open(file_path, "a") as file:
            file.write(txt4+"\n")
           with open(file_path, "a") as file:
            file.write(txt5+"\n")
           with open(file_path, "a") as file:
            file.write(txt6+"\n")
           with open(file_path, "a") as file:
            file.write(txt7+"\n")

           
           


def output():
    global rtype,scf,mcharge,mul,max
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
       #rtype=orun.get()
       # #scf=oscf.get()
       max=omax.get()
       mul=omul.get()
       mcharge=omcharge.get()
       Label(outframe,text=f"$CONTRL SCFTYP={scf.get()} RUNTYP={rtype.get()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END").place(x=430,y=230)
       Label(outframe,text=f"$SYSTEM TIMLIM=525600 MEMORY=1000000 $END").place(x=430,y=250)
       Label(outframe,text=f"$BASIS GBASIS=MINI $END").place(x=430,y=270)
       Label(outframe,text=f"$SCF DIRSCF=.TRUE. $END").place(x=430,y=290)
       Label(outframe,text=f"$DATA").place(x=430,y=310)
       Label(outframe,text=f"Title").place(x=430,y=330)
       Label(outframe,text=f"C1").place(x=430,y=350)



#Frames
upperframe=LabelFrame(root,width=1070, height=30, bg="white", bd=2).place(x=1,y=5)
listframe=LabelFrame(root,width=100, height=480, bg="white", bd=2).place(x=1,y=38)
midframe=LabelFrame(root,width=965,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
outframe=LabelFrame(root,text="Output",width=470, height=310,bd=2).place(x=420,y=200)
geobtnframe=LabelFrame(root,width=180, height=120,bd=2).place(x=640,y=50)
geoframe=LabelFrame(root,text="Geometry of the Molecule",width=150, height=460,bd=2).place(x=905,y=50)



inframe1=LabelFrame(root,width=300, height=100,bd=2).place(x=110,y=50)
inframe2=LabelFrame(root,width=300, height=70,bd=2).place(x=110,y=170)
inframe3=LabelFrame(root,width=300, height=70,bd=2).place(x=110,y=260)
inframe4=LabelFrame(root,width=200, height=120,bd=2).place(x=420,y=50)


#Buttons
upbutton1 =Button(root, text="File",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=7)
upbutton2 =Button(root, text="Edit",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=43,y=7)
upbutton3 =Button(root, text="Subwindow",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=83,y=7)
upbutton4 =Button(root, text="Help",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=163,y=7)


lbutton1 =Button(root, text="Basis",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=40)
lbutton2 =Button(root, text="Control",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=70)
lbutton3 =Button(root, text="Data",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=100)
lbutton4 =Button(root, text="System",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=130)
lbutton5 =Button(root, text="FMO",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=160)
lbutton6 =Button(root, text="MO Guess",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=190)
lbutton7 =Button(root, text="Misc. Prefs",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=220)
lbutton8 =Button(root, text="SCF Options",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=250)
lbutton9 =Button(root, text="Summary",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=280)


lowbutton1 =Button(root, text="Use Defaults",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=8,y=520)
lowbutton2 =Button(root, text="Revert",bg="white",font=("Arial",10),relief="flat",padx=10,pady=0).place(x=108,y=520)
lowbutton3 =Button(root, text="Write File",bg="white",command=save_file,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=198,y=520)
lowbutton4 =Button(root, text="Edit and Save",bg="white",command=save_file,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=288,y=520)
lowbutton5 =Button(root, text="Ok",bg="white",font=("Arial",10),relief="flat",padx=20,pady=0,command=output).place(x=532,y=520)
lowbutton6 =Button(root, text="Cancel",bg="white",command=root.destroy,font=("Arial",10),relief="flat",padx=10,pady=0).place(x=622,y=520)


open_button =Button(root, text="Open Text File", command=open_file).place(x=685,y=110)


rtype=StringVar(value="Energy")
scf=StringVar(value="RHF")

#Inner Lables:
in1lb1=Label(inframe1,text="Run Type:").place(x=115,y=55)
orun=OptionMenu(inframe1,rtype,*['Energy', 'Hessian', 'Optimization'])
orun.place(x=175, y=55)     ;     orun.configure(width=10,bg='White')
in1lb2=Label(inframe1,text="SCF Type:").place(x=115,y=95)
oscf= OptionMenu(inframe1,scf,*['UHF', 'RHF', 'ROHF'])
oscf.place(x=175, y=95)     ;     oscf.configure(width=5,bg='White')
in1lb3=Label(inframe1,text="Localization Method: None").place(x=115,y=125)



in2lb1=Label(inframe3,text="Molecule Charge:").place(x=115,y=175)
omcharge=Entry(inframe2,width=10)
omcharge.place(x=215, y=175)
in2lb2=Label(inframe3,text="Multiplicity:").place(x=115,y=205)
omul=Entry(inframe2,width=10)
omul.place(x=190, y=205)


in3lb1=Label(inframe2,text="Exe. Type: Normal Run").place(x=115,y=265)
in3lb2=Label(inframe2,text="Max # SCF Iterations:").place(x=115,y=300)
omax=Entry(inframe2,width=10)
omax.place(x=235, y=300)


in4lb1=Label(midframe,text="MP2").place(x=425,y=55)
in4lb2=Label(midframe,text="DFT").place(x=425,y=85)
in4lb3=Label(midframe,text="Cl: None").place(x=425,y=115)
in4lb4=Label(midframe,text="CC: None").place(x=425,y=145)

geolabel=Label(geoframe,text="Upload text file:").place(x=685,y=70)




root.title("Input Builder by Riddhiman Dutta(25BAI11325)")
logo=PhotoImage(file="vit logo.png")
root.iconphoto(True,logo)



root.mainloop()