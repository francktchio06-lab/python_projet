from tkinter import *
from facto import *
ma_calculatrice =Tk()
c=""

def p(b):
    global n,c
    
    n=str(b)
    e.insert(2.0,n)
    c+=str(b)


def calcul():

    global c
    try:
            c=str(eval(c))  
            e.insert(1.0,c)
            e.delete(1.0,END)
            e.insert(1.0,c)
            
    except:
            efface()
            e.insert(1.0,"erreur")
def efface ():

    global n,c
    n=c=""
    e.delete(1.0,END)
def fcto ():
    global n,c
    c=facto(int(c))
    e.delete(1.0,END)
    e.insert(1.0,c)
ma_calculatrice.title("calculatrice")
ma_calculatrice.config(bg="pink")
e=Text(ma_calculatrice,height=1,width=20,font="pink",bg="blue")
b1=Button(ma_calculatrice,text="1",command=lambda: p(1),width=3)
b1.grid(row=3,column=1)
b2=Button(ma_calculatrice,text="2",command=lambda:p(2),width=3)
b2.grid(row=3,column=2)
b3=Button(ma_calculatrice,text="3",command=lambda:p(3),width=3)
b3.grid(row=3,column=3)
b4=Button(ma_calculatrice,text="4",command=lambda:p(4),width=3)
b4.grid(row=4,column=1)
b5=Button(ma_calculatrice,text="5",command=lambda:p(5),width=3)
b5.grid(row=4,column=2)
b6=Button(ma_calculatrice,text="6",command=lambda:p(6),width=3)
b6.grid(row=4,column=3)
b7=Button(ma_calculatrice,text="7",command=lambda:p(7),width=3)
b7.grid(row=5,column=1)
b8=Button(ma_calculatrice,text="8",command=lambda:p(8),width=3)
b8.grid(row=5,column=2)
b9=Button(ma_calculatrice,text="9",command=lambda:p(9),width=3)
b9.grid(row=5,column=3)
b10=Button(ma_calculatrice,text="+",command=lambda:p("+"),width=4)
b10.grid(row=3,column=4)
b11=Button(ma_calculatrice,text="-",command=lambda:p("-"),width=4)
b11.grid(row=3,column=5)
b12=Button(ma_calculatrice,text="/",command=lambda:p("/"),width=4)
b12.grid(row=4,column=4)
b13=Button(ma_calculatrice,text="*",command=lambda:p("*"),width=4)
b13.grid(row=4,column=5)
b14=Button(ma_calculatrice,text="!",width=4,command=lambda:fcto())
b14.grid(row=5,column=5)
b15=Button(ma_calculatrice,text="0",width=4,command=lambda:p("0"))
b15.grid(row=5,column=4)
b16=Button(ma_calculatrice,text="=",command=lambda :calcul())
b16.grid(row=6,column=1)
b14=Button(ma_calculatrice,text="efface",command= lambda:efface())
b14.grid(row=6,column=2)

e.grid(row=0,columnspan=6)
ma_calculatrice.mainloop()
