from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog

root=Tk()
root.geometry("1210x550")
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
                   content = file.readlines()
                   molno=len(content)
                   Label(outframe, text=f"Number of atoms={molno}").place(x=1005,y=70)
                   global content_str,newcontent_str
                   content_str = "".join(content)
                   Label(outframe, text=content_str).place(x=1005,y=90)
                   
                   
           except Exception as e:
               text_area.delete(1.0, tk.END)
               text_area.insert(tk.END, f"Error reading file: {e}")


def gamesave_file():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,capspgroup,matrix,scfval,memsize
    memsize=int(memvalue.get())
    max=omax.get()
    mul=omul.get()
    matrix=zmat.get()
    scfval=scc.get()
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G':
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G':
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
               
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get() 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()                    
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()                    
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()  
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()  
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":  
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get() 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get() 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
              
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
            if scf.get()=="RHF" or scf.get()=="ROHF":
              if pgroup.get()=="C1":
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
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

            elif scf.get()=="UHF":
              if pgroup.get()=="C1":
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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

                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                
                elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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

                elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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
                
                elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 tex1=Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END")
                 tex2=Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*131072} $END")
                 tex3=Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END")
                 tex4=Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END")
                 tex5=Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END")
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


def output():
    global rtype,scf,mcharge,mul,max,pgroup,title,miniopt,omcharge,omul,omax,matrix,scfval,memsize,capspgroup
    if not rtype.get() or not scf.get() or not omcharge.get() or not omul.get() or not omax.get():
     mb.showerror('Fields empty!', "Please fill all the missing fields !")
    else:
       memsize=int(memvalue.get())
       matrix=zmat.get()
       scfval=scc.get()
       max=omax.get()
       mul=omul.get()
       capspgroup=pgroup.get()
       mcharge=omcharge.get()
       if rtype.get()=="Energy":
        if pgroup.get()=="C1":
         if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
          Label(outframe,text=f"$CONTRL SCFTYP={scf.get()} RUNTYP={rtype.get()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f"$SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f"$BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
          Label(outframe,text=f"$SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f"$DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G':
          gbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
        elif pgroup.get()=="CS" or pgroup.get()=="CI":
         if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G':
          gbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
        elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
         if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=320)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
          gbasisk=miniopt.get() 
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=320)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get()                    
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=320)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $DATA").place(x=430,y=280)
          Label(outframe,text=f"{title.get()}").place(x=430,y=300)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=320)
       elif rtype.get()=="Optimization":
        if pgroup.get()=="C1":
         if miniopt.get()=="MINI" or miniopt.get()=="MIDI":
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G':
          gbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get()  
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get()  
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
          gbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get() 
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get() 
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
        elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
         if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
         elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
          gbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
         elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
         elif miniopt.get()=='6-311G':
          jodbasisk=miniopt.get()
          Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={"OPTIMIZE"} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
          Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
          Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
          Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
          Label(outframe,text=f" $STATPT OPTTOL=0.0001 NSTEP=20 $END").place(x=430,y=280)
          Label(outframe,text=f" $DATA").place(x=430,y=300)
          Label(outframe,text=f"{title.get()}").place(x=430,y=320)
          Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
       elif rtype.get()=="Hessian":
        if scf.get()=="RHF" or scf.get()=="ROHF":
         if pgroup.get()=="C1":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
                 gbasisk=miniopt.get()
                 Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
                 Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
                 Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
                 Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
                 Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
                 Label(outframe,text=f" $DATA").place(x=430,y=300)
                 Label(outframe,text=f"{title.get()}").place(x=430,y=320)
                 Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
                 jodbasisk=miniopt.get()
                 Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
                 Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
                 Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
                 Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
                 Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
                 Label(outframe,text=f" $DATA").place(x=430,y=300)
                 Label(outframe,text=f"{title.get()}").place(x=430,y=320)
                 Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
                 jodbasisk=miniopt.get()
                 Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
                 Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
                 Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
                 Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
                 Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
                 Label(outframe,text=f" $DATA").place(x=430,y=300)
                 Label(outframe,text=f"{title.get()}").place(x=430,y=320)
                 Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif pgroup.get()=="CS" or pgroup.get()=="CI":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
            gbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
            gbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=ANALYTIC VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f"{title.get()}").place(x=430,y=300)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=320)
        elif scf.get()=="UHF":
         if pgroup.get()=="C1":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=200)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=260)
            Label(outframe,text=f" $DATA").place(x=430,y=280)
            Label(outframe,text=f"{title.get()}").place(x=430,y=300)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=320)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
            gbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif pgroup.get()=="CS" or pgroup.get()=="CI":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI":   
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
            gbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{pgroup.get()}").place(x=430,y=340)
         elif pgroup.get()=="Cn" or pgroup.get()=="CnH" or pgroup.get()=="CnV":
          if miniopt.get()=="MINI" or miniopt.get()=="MIDI": 
           Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
           Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
           Label(outframe,text=f" $BASIS GBASIS={miniopt.get()} $END").place(x=430,y=240)
           Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
           Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
           Label(outframe,text=f" $DATA").place(x=430,y=300)
           Label(outframe,text=f"{title.get()}").place(x=430,y=320)
           Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='STO-2G' or miniopt.get()=='STO-3G'or miniopt.get()=='STO-4G' or miniopt.get()=='STO-5G' or miniopt.get()=='STO-6G': 
           gbasisk=miniopt.get()
           Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
           Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
           Label(outframe,text=f" $BASIS GBASIS=STO NGAUSS={gbasisk[4]} $END").place(x=430,y=240)
           Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
           Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
           Label(outframe,text=f" $DATA").place(x=430,y=300)
           Label(outframe,text=f"{title.get()}").place(x=430,y=320)
           Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='3-21G' or miniopt.get()=='6-21G' or miniopt.get()=='4-31G' or miniopt.get()=='5-31G' or miniopt.get()=='6-31G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:4]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)
          elif miniopt.get()=='6-311G':
            jodbasisk=miniopt.get()
            Label(root,text=f" $CONTRL SCFTYP={scf.get()} RUNTYP={(rtype.get()).upper()} MAXIT={max} ICHARG={mcharge} MULT={mul} NZVAR={matrix} $END").place(x=430,y=200)
            Label(outframe,text=f" $SYSTEM TIMLIM=525600 MEMORY={memsize*128072} $END").place(x=430,y=220)
            Label(outframe,text=f" $BASIS GBASIS=N{jodbasisk[2:5]} NGAUSS={jodbasisk[0]} $END").place(x=430,y=240)
            Label(outframe,text=f" $SCF DIRSCF=.TRUE. NCONV={scfval} $END").place(x=430,y=260)
            Label(outframe,text=f" $FORCE METHOD=SEMINUM VIBSIZ=0.010000 VIBANL=.TRUE. $END").place(x=430,y=280)
            Label(outframe,text=f" $DATA").place(x=430,y=300)
            Label(outframe,text=f"{title.get()}").place(x=430,y=320)
            Label(outframe,text=f"{capspgroup.upper()} 2").place(x=430,y=340)

def control():
  global omcharge,omax,omul,outframe,geobtnframe,geoframe,logopic
  ctrlmidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)

  outframe=LabelFrame(ctrlmidframe,text="Output",width=520, height=185,bd=2).place(x=420,y=180)
  geobtnframe=LabelFrame(ctrlmidframe,width=300, height=120,bd=2).place(x=640,y=50)
  geoframe=LabelFrame(ctrlmidframe,text="Geometry of the Molecule",width=240, height=465,bd=2).place(x=955,y=45)
  filewritebtnframe=LabelFrame(ctrlmidframe,width=300, height=160,bd=2).place(x=110,y=350)



  inframe1=LabelFrame(ctrlmidframe,width=300, height=100,bd=2).place(x=110,y=50)
  inframe2=LabelFrame(ctrlmidframe,width=300, height=70,bd=2).place(x=110,y=170)
  inframe3=LabelFrame(ctrlmidframe,width=300, height=70,bd=2).place(x=110,y=260)
  inframe4=LabelFrame(ctrlmidframe,width=200, height=120,bd=2).place(x=420,y=50)

  open_button =Button(geobtnframe, text="Open Geometry File", command=open_file,width=30,height=2).place(x=685,y=110)
  psi_button =Button(filewritebtnframe, text="Write Psi4 File", command=psisave_file,height=2,width=15).place(x=130,y=395)
  games_button =Button(filewritebtnframe, text="Write GAMESS File", command=gamesave_file,height=2,width=15).place(x=270,y=395)
  outbtn=Button(filewritebtnframe, text="Output", command=output,height=2,width=15).place(x=270,y=460)

  psilbl=Label(filewritebtnframe,text="For Psi4 File:").place(x=130,y=365)
  gamelbl=Label(filewritebtnframe,text="For GAMESS File:").place(x=270,y=365)
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

  geolabel=Label(geoframe,text="Upload Geometry(text) file of Molecule:").place(x=720,y=70)

  logopic=PhotoImage(file="smallRids.png")
  logo_label=Label(ctrlmidframe,image=logopic).place(x=550,y=380) 

  outlbl=Label(filewritebtnframe,text=" Preview Output:").place(x=130,y=470)


def basis():
  global miniopt
  basmidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  bas1=Label(basmidframe,text="Basis Set :").place(x=135,y=50)

  basmenu=OptionMenu(basmidframe,miniopt,*['MINI', 'MIDI','STO-2G','STO-3G','STO-4G','STO-5G','STO-6G','3-21G','6-21G','4-31G','5-31G','6-31G','6-311G'])
  basmenu.place(x=210, y=45)     ;     basmenu.configure(width=10,bg='White')


  bas2=Label(basmidframe,text="# D heavy atom polarization functions :    0").place(x=135,y=85)
  bas3=Label(basmidframe,text="# F heavy atom polarization functions :    0").place(x=135,y=120)
  bas4=Label(basmidframe,text="# light atom polarization functions :      0").place(x=135,y=155)
  

  



def data():
  datamidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #Data Inner Labels
  global title,zmat
  title=Entry(datamidframe,width=50)
  title.place(x=130,y=45)
  title.insert(0,"Title")
  datainframe1=LabelFrame(root,width=300, height=110,bd=2).place(x=130,y=100)
  datainframe2=LabelFrame(root,width=300, height=90,bd=2).place(x=130,y=240)


  data1in1lb1=Label(datainframe1,text="Coord. Type :       Unique Cartesian Coords.").place(x=135,y=110)
  data2in1lb1=Label(datainframe1,text="Units :      Angstroms").place(x=135,y=145)
  datain1lb1=Label(datainframe1,text="# of Z-Matrix Varibles:").place(x=135,y=180)
  zmat=Entry(datainframe1)
  zmat.place(x=270,y=180)
  zmat.insert(0,"0")

  data1in1lb2=Label(datainframe2,text="Point Group :")
  data1in1lb2.place(x=135,y=255)
  data2in1lb2=Label(datainframe2,text="Order of Principle Axis :   000000").place(x=135,y=295)
  
  datamenu=OptionMenu(datainframe2,pgroup,*['C1', 'CS','CI','CnH','CnV','Cn'])
  datamenu.place(x=240, y=255)     ;     datamenu.configure(width=10,bg='White')



def sys():
  global memvalue
  sysmidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  sys1=Label(sysmidframe,text="Time Limit : 525600.00").place(x=135,y=50)
  sys2=Label(sysmidframe,text="Memory(MB):").place(x=135,y=85)
  sys3=Label(sysmidframe,text="MemDDI :    0.00").place(x=135,y=120)
  sys4=Label(sysmidframe,text="Diagonalization Method :    default").place(x=135,y=155)
  sys5=Label(sysmidframe,text="Parallel Load Balance Type :    Loop").place(x=135,y=190)
  memvalue=Entry(sysmidframe,width=30)
  memvalue.place(x=240,y=85)
  memvalue.insert(0,"10")



def mo():
  momidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  mo1=Label(momidframe,text="Initial Guess : Huckel").place(x=135,y=50)
  mo2=Label(momidframe,text="$VEC source :    000000").place(x=135,y=85)


def scfopt():
  global scc
  scfmidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
  #System Inner Labels
  scf1=Label(scfmidframe,text="Direct SCF").place(x=135,y=50)
  scf2=Label(scfmidframe,text="Compute only change in Fock Matrix").place(x=135,y=85)
  scf2=Label(scfmidframe,text="SCF Convergence Criteria :    10 ^ ").place(x=135,y=120)
  scc=Entry(scfmidframe,width=20)
  scc.place(x=325,y=120)
  scc.insert(0,"5")


def summary():
    summidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
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
    
def home():
 global logopic
 logomidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)  
 logopic=PhotoImage(file="rids.png")
 logo_label=Label(logomidframe,image=logopic).place(x=200,y=70)  

def about():
 aboutmidframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)
 aboutlbl=Label(aboutmidframe,text="About Us",fg="red", font=("Arial",22))
 aboutlbl.place(x=610,y=70)
 Label(aboutmidframe,fg="blue",text="Traditionally, chemists have relied on text editors or command\nline tools to generate input files for quantum chemistry software, \nmaking the process time-consuming and prone to errors. \nThe RIDS Input Builder App addresses this gap by providing an intuitive,\nuser-friendly interface designed specifically for the quantum chemistry community.", font=("Arial",16)).place(x=310,y=120)
 Label(aboutmidframe,fg="blue",text="Unlike most existing solutions, this app allows users to input data\nand instantly receive outputs in multiple formats, facilitating\nseamless transfer to quantum chemistry packages such as\nChemCompute, GAMESS, or PSI4. Its multiformat support streamlines\nworkflow and significantly reduces the learning\ncurve for new users, while also catering to advanced needs through\nflexible output options.", font=("Arial",16)).place(x=360,y=240)
 Label(aboutmidframe,text="Developed and Designed by Riddhiman Dutta.",fg="red" ,font=("Arial",16)).place(x=460,y=420)
 Label(aboutmidframe,text="Email-riddhiman93@gmail.com",fg="red" ,font=("Arial",16)).place(x=550,y=450)
 

#Variables
rtype=StringVar(value="Energy")
scf=StringVar(value="RHF")
pgroup=StringVar(value="C1")
title=StringVar(value="Title")
miniopt=StringVar(value="MINI")
memvalue=StringVar(value=10)
zmat=StringVar(value=0)
scc=StringVar(value=5)


#Frames
upperframe=LabelFrame(root,width=1210, height=30, bg="white", bd=2).place(x=1,y=5)
listframe=LabelFrame(root,width=100, height=480, bg="white", bd=2).place(x=1,y=38)
midframe=LabelFrame(root,width=1105,relief=SUNKEN, height=480,bd=2).place(x=105,y=38)

#Buttons
upbutton1 =Button(root, text="Home",bg="white",command=home,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=3,y=7)
upbutton2 =Button(root, text="Save",bg="white",command=gamesave_file,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=53,y=7)
upbutton3 =Button(root, text="About",bg="white",command=about,font=("Arial",10),relief="flat",padx=0,pady=0).place(x=103,y=7)


lbutton1 =Button(root, text="Basis",bg="white",command=basis,font=("Arial",10),relief="flat",padx=25,pady=0).place(x=3,y=40)
lbutton2 =Button(root, text="Control",bg="white",command=control,font=("Arial",10),relief="flat",padx=22,pady=0).place(x=3,y=70)
lbutton3 =Button(root, text="Data",bg="white",command=data,font=("Arial",10),relief="flat",padx=29,pady=0).place(x=3,y=100)
lbutton4 =Button(root, text="System",bg="white",command=sys,font=("Arial",10),relief="flat",padx=20,pady=0).place(x=3,y=130)
lbutton5 =Button(root, text="SCF Options",bg="white",command=scfopt,font=("Arial",10),relief="flat",padx=5,pady=0).place(x=3,y=160)
lbutton6 =Button(root, text="Summary",bg="white",command=summary,font=("Arial",10),relief="flat",padx=15,pady=0).place(x=3,y=190)



lowbutton =Button(root, text="Close",bg="white",command=root.destroy,font=("Arial",10),relief="flat",padx=30,pady=0).place(x=580,y=520)

photo=PhotoImage(file="rids.png")
pic_label=Label(midframe,image=photo)
pic_label.place(x=200,y=70)  


root.title("RIDS Chemistry Input Builder App by Riddhiman Dutta")
logo=PhotoImage(file="rids.png")
root.iconphoto(True,logo)



root.mainloop()

