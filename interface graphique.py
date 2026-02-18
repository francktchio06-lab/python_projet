from tkinter import *
from tkinter import ttk
root= Tk()
root.config(bg="white")
root.title("respecte tes heures")
root.geometry("1000x700")
def p(n):
    e.config(state="normal")
    e.delete(0,20)
    e.insert(1_0,n)
e=Entry(root,bg="purple",width=500,font="algerian")
f=Frame(root,bg="purple",width="100",height="1000")
b=Button(f,text="enseignant",command=lambda:p("enseignant"),bg="purple",bd="0")
b1=Button(f,text="filière",command=lambda:p("filière"),bg="purple",bd="0")
b2=Button(f,text="heure",command=lambda:p("heure"),bg="purple",bd="0")
b3=Button(f,text="y ajouter?",command=lambda:p("y ajouter? "),bg="purple",bd="0")
l=Label(f,text="rubrique" ,bg="purple",font=15)

l1=["bts1","bts2","licence ", "master1","master2","cp1","cp2"]
h=ttk.Combobox(root,values=l1)
h.place(x=250,y=150)
e.place(x=100,y=0)
f.place(x=0,y=0)
b.place(x=10,y=50,width=75)
b1.place(x=10,y=150,width=75)
b2.place(x=10,y=250,width=75)
b3.place(x=10,y=350,width=75)
l.place(x=10,y=10)
root.mainloop()