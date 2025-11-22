from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog

#LabelFrame(root,width=100, height=350,bd=2).place(x=500,y=350),LabelFrame(root,width=100, height=350,bd=2).place(x=500,y=350)


root=Tk()
root.geometry("1160x550")
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
                   line2=file.readline()
                   #molno=int(line1)
                   #Label(outframe, text=f"Number of atoms={molno}").place(x=915,y=70)

                   content = file.readlines()
                   molno=len(content)
                   Label(outframe, text=f"Number of atoms={molno}").place(x=915,y=70)
                   global content_str,newcontent_str
                   content_str = "".join(content)
                   Label(outframe, text=content_str).place(x=915,y=90)
                   
                   
           except Exception as e:
               text_area.delete(1.0, tk.END)
               text_area.insert(tk.END, f"Error reading file: {e}")





def gamesave_file():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,capspgroup
    max=omax.get()
    mul=omul.get()
    capspgroup=pgroup.get()
    mcharge=omcharge.get()
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
           # Get all text from the Text widget
           if rtype.get()=="Energy":
              if pgroup.get()=="C1":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $DATA")
                tex6=Label(outframe,text=f"{title.get()}")
                tex7=Label(outframe,text=f"{pgroup.get()}")
              

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
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")
              
              elif pgroup.get()=="CS" or pgroup.get()=="CI":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $DATA")
                tex6=Label(outframe,text=f"{title.get()}")
                tex7=Label(outframe,text=f"{pgroup.get()}")
              

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
                with open(file_path, "a") as file:
                 file.write("\n")  
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")

              elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $DATA")
                tex6=Label(outframe,text=f"{title.get()}")
                tex7=Label(outframe,text=f"{capspgroup.upper()} 2")
              

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
                with open(file_path, "a") as file:
                 file.write("\n")  
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")          


            
           
           elif rtype.get()=="Optimization":
              if pgroup.get()=="C1":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{pgroup.get()}")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")
              elif pgroup.get()=="CS"or pgroup.get()=="CI":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{pgroup.get()}")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write("\n")  
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")
              
              elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{capspgroup.upper()} 2")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write("\n")  
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")


           elif rtype.get()=="Hessian":
              if pgroup.get()=="C1":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{pgroup.get()}")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")

              elif pgroup.get()=="CS" or pgroup.get()=="CI":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{pgroup.get()}")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write("\n")
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")

                
              elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
                tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} $END")
                tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY=1000000 $END")
                tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. $END")
                tex5=Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END")
                tex6=Label(outframe,text=f" $DATA")
                tex7=Label(outframe,text=f"{title.get()}")
                tex8=Label(outframe,text=f"{capspgroup.upper()} 2")


                txt1=tex1.cget("text")
                txt2=tex2.cget("text")
                txt3=tex3.cget("text")
                txt4=tex4.cget("text")
                txt5=tex5.cget("text")
                txt6=tex6.cget("text")
                txt7=tex7.cget("text")
                txt8=tex8.cget("text")

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
                with open(file_path, "a") as file:
                 file.write(txt8+"\n")
                with open(file_path, "a") as file:
                 file.write("\n")
                with open(file_path, "a") as file:
                 file.write(content_str)
                with open(file_path, "a") as file:
                 file.write(" $END"+"\n")





def psisave_file():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,memvalue
    max=omax.get()
    mul=omul.get()
    mcharge=omcharge.get()
    memory=memvalue.get()
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
           # Get all text from the Text widget
           if rtype.get()=="Energy":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"energy('scf')")
              


              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")
            
           elif rtype.get()=="Optimization":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"optimization('scf')")
              


              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")


           elif rtype.get()=="Hessian":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"hessian('scf')")
              


              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")





def energydistsave_file():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,memvalue
    max=omax.get()
    mul=omul.get()
    mcharge=omcharge.get()
    memory=memvalue.get()
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
           # Get all text from the Text widget
           if rtype.get()=="Energy":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis aug-cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"energy('sapt0')")
              tex5=Label(outframe,text=f"symmetry {pgroup.get()}")
              


              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              txt5=tex5.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)              
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write("units angstrom"+"\n")
              with open(file_path, "a") as file:
               file.write("no_reorient"+"\n")
              with open(file_path, "a") as file:
               file.write(txt5+"\n")
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")
            
           elif rtype.get()=="Optimization":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis aug-cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"optimization('scf')")
              tex5=Label(outframe,text=f"symmetry {pgroup.get()}")

              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              txt5=tex5.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)              
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write("units angstrom"+"\n")
              with open(file_path, "a") as file:
               file.write("no_reorient"+"\n")
              with open(file_path, "a") as file:
               file.write(txt5+"\n")
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")


           elif rtype.get()=="Hessian":
              tex1=Label(root,text=f"memory {memory} mb")
              tex2=Label(outframe,text="molecule  {")
              tex3=Label(outframe,text=f"set basis aug-cc-{miniopt.get()}")
              tex4=Label(outframe,text=f"hessian('scf')")
              tex5=Label(outframe,text=f"symmetry {pgroup.get()}")

              txt1=tex1.cget("text")
              txt2=tex2.cget("text")
              txt3=tex3.cget("text")
              txt4=tex4.cget("text")
              txt5=tex5.cget("text")
              

              # Write the content to the selected file
              with open(file_path, "w") as file:
                file.write(txt1+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt2+"\n")
              with open(file_path, "a") as file:
               file.write(content_str)              
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write("units angstrom"+"\n")
              with open(file_path, "a") as file:
               file.write("no_reorient"+"\n")
              with open(file_path, "a") as file:
               file.write(txt5+"\n")
              with open(file_path, "a") as file:
               file.write("}"+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
                file.write(txt3+"\n")
              with open(file_path, "a") as file:
                file.write("\n")
              with open(file_path, "a") as file:
               file.write(txt4+"\n")





def output():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,omcharge,omul,omax
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
       Label(outframe,text=f"$BASIS GBASIS={miniopt.get()} $END").place(x=430,y=270)
       Label(outframe,text=f"$SCF DIRSCF=.TRUE. $END").place(x=430,y=290)
       Label(outframe,text=f"$DATA").place(x=430,y=310)
       Label(outframe,text=f"{title.get()}").place(x=430,y=330)
       Label(outframe,text=f"{pgroup.get()}").place(x=430,y=350)


def control():
  global omcharge,omax,omul,outframe,geobtnframe,geoframe
  ctrlmidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)

  outframe=LabelFrame(ctrlmidframe,text="Output",width=470, height=310,bd=2).place(x=420,y=200)
  geobtnframe=LabelFrame(ctrlmidframe,width=180, height=120,bd=2).place(x=640,y=50)
  geoframe=LabelFrame(ctrlmidframe,text="Geometry of the Molecule",width=240, height=460,bd=2).place(x=905,y=50)
  filewritebtnframe=LabelFrame(ctrlmidframe,width=300, height=120,bd=2).place(x=110,y=350)



  inframe1=LabelFrame(ctrlmidframe,width=300, height=100,bd=2).place(x=110,y=50)
  inframe2=LabelFrame(ctrlmidframe,width=300, height=70,bd=2).place(x=110,y=170)
  inframe3=LabelFrame(ctrlmidframe,width=300, height=70,bd=2).place(x=110,y=260)
  inframe4=LabelFrame(ctrlmidframe,width=200, height=120,bd=2).place(x=420,y=50)

  open_button =Button(geobtnframe, text="Open Text File", command=open_file).place(x=685,y=110)
  psi_button =Button(filewritebtnframe, text="Write Psi4 File", command=psisave_file).place(x=130,y=410)
  games_button =Button(filewritebtnframe, text="Write GAMESS File", command=gamesave_file).place(x=270,y=410)
  energydistbtn=Button(ctrlmidframe, text="Energy Distribution File", command=energydistsave_file).place(x=180,y=480)

  psilbl=Label(filewritebtnframe,text="For Psi4 File:").place(x=130,y=370)
  gamelbl=Label(filewritebtnframe,text="For GAMESS File:").place(x=270,y=370)
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
  omcharge.insert(0,"0")
  in2lb2=Label(inframe3,text="Multiplicity:").place(x=115,y=205)
  omul=Entry(inframe2,width=10)
  omul.place(x=190, y=205)
  omul.insert(0,"1")


  in3lb1=Label(inframe2,text="Exe. Type: Normal Run").place(x=115,y=265)
  in3lb2=Label(inframe2,text="Max # SCF Iterations:").place(x=115,y=300)
  omax=Entry(inframe2,width=10)
  omax.place(x=235, y=300)
  omax.insert(0,"30")


  in4lb1=Label(ctrlmidframe,text="MP2").place(x=425,y=55)
  in4lb2=Label(ctrlmidframe,text="DFT").place(x=425,y=85)
  in4lb3=Label(ctrlmidframe,text="CI: None").place(x=425,y=115)
  in4lb4=Label(ctrlmidframe,text="CC: None").place(x=425,y=145)

  geolabel=Label(geoframe,text="Upload text file:").place(x=685,y=70)


def basis():
  global miniopt
  basmidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  bas1=Label(basmidframe,text="Basis Set :").place(x=135,y=50)

  basmenu=OptionMenu(basmidframe,miniopt,*['MINI', 'MIDI','STO-2G','STO-3G','STO-4G','STO-5G','STO-6G','3-21G','6-21G','4-31G','5-31G','6-31G','6-311G'])
  basmenu.place(x=210, y=45)     ;     basmenu.configure(width=10,bg='White')


  bas2=Label(basmidframe,text="# D heavy atom polarization functions :    0").place(x=135,y=85)
  bas3=Label(basmidframe,text="# F heavy atom polarization functions :    0").place(x=135,y=120)
  bas4=Label(basmidframe,text="# light atom polarization functions :      0").place(x=135,y=155)
  

  



def data():
  datamidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #Data Inner Labels
  global title
  title=Entry(datamidframe,width=50)
  title.place(x=130,y=45)
  title.insert(0,"Title")
  datainframe1=LabelFrame(root,width=300, height=110,bd=2).place(x=130,y=100)
  datainframe2=LabelFrame(root,width=300, height=90,bd=2).place(x=130,y=240)


  data1in1lb1=Label(datainframe1,text="Coord. Type :       Unique Cartesian Coords.").place(x=135,y=110)
  data2in1lb1=Label(datainframe1,text="Units :      Angstroms").place(x=135,y=145)
  datain1lb1=Label(datainframe1,text="# of Z-Matrix Varibles:").place(x=135,y=180)
  Entry(datainframe1).place(x=270,y=180)

  data1in1lb2=Label(datainframe2,text="Point Group :")
  data1in1lb2.place(x=135,y=255)
  data2in1lb2=Label(datainframe2,text="Order of Principle Axis :   000000").place(x=135,y=295)
  
  datamenu=OptionMenu(datainframe2,pgroup,*['C1', 'CS','CI','CnH','CnV','Cn'])
  datamenu.place(x=240, y=255)     ;     datamenu.configure(width=10,bg='White')



def sys():
  sysmidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  sys1=Label(sysmidframe,text="Time Limit : 525600.00").place(x=135,y=50)
  sys2=Label(sysmidframe,text="Memory(MB):").place(x=135,y=85)
  sys3=Label(sysmidframe,text="MemDDI :    0.00").place(x=135,y=120)
  sys4=Label(sysmidframe,text="Diagonalization Method :    default").place(x=135,y=155)
  sys5=Label(sysmidframe,text="Parallel Load Balance Type :    Loop").place(x=135,y=190)
  global memvalue
  memvalue=Entry(sysmidframe,width=30)
  memvalue.place(x=240,y=85)



def mo():
  momidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  mo1=Label(momidframe,text="Initial Guess : Huckel").place(x=135,y=50)
  mo2=Label(momidframe,text="$VEC source :    000000").place(x=135,y=85)


def scfopt():
  scfmidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  scf1=Label(scfmidframe,text="Direct SCF").place(x=135,y=50)
  scf2=Label(scfmidframe,text="Compute only change in Fock Matrix").place(x=135,y=85)
  scf2=Label(scfmidframe,text="SCF Convergence Criteria :    10 ^ ").place(x=135,y=120)
  scc=Entry(scfmidframe,width=20)
  scc.place(x=325,y=120)
  scc.insert(0,5)


def summary():
    summidframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
    global title, pgroup,miniopt,rtype,scf
    sum1=Label(text=f"Title :      {title.get()}")
    sum1.place(x=135,y=50)
    sum2=Label(text=f"Molecular Point Group :     {pgroup.get()} ")
    sum2.place(x=135,y=85)
    sum3=Label(text=f"Basis Set :     {miniopt.get()} ")
    sum3.place(x=135,y=120)
    sum4=Label(text=f"Run Type :     {rtype.get()} ")
    sum4.place(x=135,y=155)
    sum5=Label(text=f"SCF :     {scf.get()} ")
    sum5.place(x=135,y=190)
    


rtype=StringVar(value="Energy")
scf=StringVar(value="RHF")
pgroup=StringVar(value="C1")
title=StringVar(value="Title")
miniopt=StringVar(value="MINI")
memvalue=StringVar(value="500")


#Frames
upperframe=LabelFrame(root,width=1160, height=30, bg="white", bd=2).place(x=1,y=5)
listframe=LabelFrame(root,width=100, height=480, bg="white", bd=2).place(x=1,y=38)
midframe=LabelFrame(root,width=1055,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)

#Buttons
upbutton1 =Button(root, text="File",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=7)
upbutton2 =Button(root, text="Edit",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=43,y=7)
upbutton3 =Button(root, text="Subwindow",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=83,y=7)
upbutton4 =Button(root, text="Help",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=163,y=7)


lbutton1 =Button(root, text="Basis",bg="white",command=basis,font=("Arial",10),relief="flat",padx=25,pady=0).place(x=3,y=40)
lbutton2 =Button(root, text="Control",bg="white",command=control,font=("Arial",10),relief="flat",padx=22,pady=0).place(x=3,y=70)
lbutton3 =Button(root, text="Data",bg="white",command=data,font=("Arial",10),relief="flat",padx=29,pady=0).place(x=3,y=100)
lbutton4 =Button(root, text="System",bg="white",command=sys,font=("Arial",10),relief="flat",padx=20,pady=0).place(x=3,y=130)
lbutton5 =Button(root, text="SCF Options",bg="white",command=scfopt,font=("Arial",10),relief="flat",padx=5,pady=0).place(x=3,y=160)
lbutton6 =Button(root, text="Summary",bg="white",command=summary,font=("Arial",10),relief="flat",padx=15,pady=0).place(x=3,y=190)


lowbutton1 =Button(root, text="Use Defaults",bg="white",font=("Arial",10),relief="flat",padx=0,pady=0).place(x=8,y=520)
lowbutton2 =Button(root, text="Revert",bg="white",font=("Arial",10),relief="flat",padx=10,pady=0).place(x=108,y=520)
lowbutton3 =Button(root, text="Write File",bg="white",command=gamesave_file,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=198,y=520)
lowbutton4 =Button(root, text="Edit and Save",bg="white",command=gamesave_file,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=288,y=520)
lowbutton5 =Button(root, text="Ok",bg="white",font=("Arial",10),relief="flat",padx=20,pady=0,command=output).place(x=532,y=520)
lowbutton6 =Button(root, text="Cancel",bg="white",command=root.destroy,font=("Arial",10),relief="flat",padx=10,pady=0).place(x=622,y=520)



#ridframe=LabelFrame(root,width=950, height=420,bd=2).place(x=160,y=75)

photo=PhotoImage(file="C:\\Users\\riddh\\Downloads\\rids.png")
pic_label=Label(midframe,image=photo)
pic_label.place(x=200,y=70)  


root.title("RIDS Chemistry Input Builder App by Riddhiman Dutta(25BAI11325)")
logo=PhotoImage(file="C:\\Users\\riddh\\Downloads\\rids.png")
root.iconphoto(True,logo)



root.mainloop()