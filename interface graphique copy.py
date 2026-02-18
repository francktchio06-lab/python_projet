from tkinter import *
from tkinter import ttk
import os
import sqlite3
from base import *
from tkinter import messagebox as box
from bar import *


root= Tk()
root.config(bg="white")
root.title("respecte tes heures")
root.geometry("1000x700")

 
def p(n):
    e.config(state="normal")
    e.delete(0,20)
    e.insert(1_0,n)
    f=Frame(root,width=3000,height="1000",bg="purple")
    f.place(x=100,y=20)
   
    
    if n=="enseignant":
        l=Label(f,text="nom",font=15,bg="purple")
        l.place(x=100,y=30)
        l=Label(f,text="filières",font=15,bg="purple")
        l.place(x=100,y=90)
        l=Label(f,text="niveau",font=15,bg="purple")
        l.place(x=100,y=150)
        l=Label(f,text="heure de cours total",font=15,bg="purple")
        l.place(x=100,y=210)
        l=Label(f,text="matricule",font=15,bg="purple")
        l.place(x=100,y=270)
        l=Label(f,text="heure par jour",font=15,bg="purple")
        l.place(x=100,y=330)
        e5=Entry(f,width=45)
        e5.place (x=250,y=30)
        
        e1=Entry(f,width=45)
        e1.place (x=250,y=90)
        e2=Entry(f,width=45)
        e2.place(x=250,y=270)
            
        # Créer une barre de défilement
        
        e3=Entry(f,width=4)
        e3.place (x=300,y=210)
        e4=Entry(f,width=4)
        e4.place(x=300,y=330)
        
        
        
        l=["bts1","bts2","licence ", "master1","master2","cp1","cp2"]
        h=ttk.Combobox(f,values=l)
        h.place(x=250,y=150)
        def ajouter():
            Nom = e5.get()
            Prenoms = e1.get()
            matricule=e2.get()
            heure_total = e3.get()
            Filiere = h.get()
            heure_jour=e4.get()
            if not (  Nom and Prenoms and   heure_total and Filiere ):
             box.showerror("ERROR","Veuillez entrer toutes les informations")
            else:

        #connexion
             con = sqlite3.connect('base.db')
             cuser = con.cursor()
             cuser.execute("insert into enseignant('Nom','Prenoms','heure_total','Filiere',Matricule,heure_jour) values (?,?,?,?,?,?)",(Nom,Prenoms,heure_total,Filiere,matricule,heure_jour))
             con.commit()
             con.close()
             box.showinfo("sucess","ajouter")
    
            #afficher
             con = sqlite3.connect('base.db')
             cuser = con.cursor()
             select = cuser.execute("select *from base order by Matricule desc")
             select = list(select)
             table.insert('',END,values = select[0])
             con.close()

        register=Button(f,text="soumettre",command=lambda:ajouter())
        register.place(x=250 ,y=400)
    if n=="filière":
        
        l=Label(f,text="niveau",font=15,bg="purple")
        l.place(x=100,y=30)
        l=Label(f,text="matière",font=15,bg="purple")
        l.place(x=100,y=90)
        l=Label(f,text="heure par jour",font=15,bg="purple")
        l.place(x=100,y=150)
        l=Label(f,text="heure de cours total",font=15,bg="purple")
        l.place(x=100,y=210)
       
        e1=Entry(f,width=45)
        e1.place (x=250,y=90)
        e2=Entry(f,width=4)
        e2.place (x=250,y=150)
        e3=Entry(f,width=4)
        l=["bts1","bts2","licence ", "master1","master2","cp1","cp2"]
        h=ttk.Combobox(f,values=l)
        h.place(x=250,y=30)
        e3.place (x=300,y=210)
        def ajouter2():
            Niveaux = h.get()
            matière = e1.get()
            heure_jour=e2.get()
            heure_total = e3.get()
            if not (  Niveaux and matière and   heure_total and heure_jour ):
             box.showerror("ERROR","Veuillez entrer toutes les informations")
            else:

        #connexion
             con = sqlite3.connect('base.db')
             cuser = con.cursor()
             cuser.execute("insert into filière('niveau','matière','heure_total','heure_jour') values (?,?,?,?)",(Niveaux,matière,heure_total,heure_jour))
             con.commit()
             con.close()
             box.showinfo("sucess","ajouter")
    
            #afficher
             con = sqlite3.connect('base.db')
             cuser = con.cursor()
             select = cuser.execute("select *from base order by Matricule desc")
             select = list(select)
             table.insert('',END,values = select[0])
             con.close()
        register=Button(f,text="soumettre",command=lambda:ajouter2())
        register.place(x=250 ,y=400)
        if n=="diagramme":
            d=button(f,text="tracer",command=lambda:diagrame())
            d.place(x=250,y=400)

        
        
        


e=Entry(root,bg="purple",width=500,font="algerian")
f=Frame(root,bg="purple",width="100",height="1000")
b=Button(f,text="enseignant",command=lambda:p("enseignant"),bg="purple",bd="0")
b1=Button(f,text="filière",command=lambda:p("filière"),bg="purple",bd="0")
b2=Button(f,text="diagramme",command=lambda:diagrame(),bg="purple",bd="0")
b3=Button(f,text="pourcentage",command=lambda:p("y ajouter? "),bg="purple",bd="0")
l=Label(f,text="rubrique" ,bg="purple",font=15)

e.place(x=100,y=0)
f.place(x=0,y=0)
b.place(x=10,y=50,width=75)
b1.place(x=10,y=150,width=75)
b2.place(x=10,y=250,width=75)
b3.place(x=10,y=350,width=75)
l.place(x=10,y=10)
root.mainloop()
