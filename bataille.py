from math import *
from random import *
from time import *
x=randint(1,100)
y=randint(1,100)
c=int(input("saisir l'abscise de votre bateau "))
z=int(input("saisir l'ordonné de votre bateau "))
raté=0
for i in range(5): 
    a=int(input("saisir l'abscise de votre bateau ennemi "))
    b=int(input("saisir l'abscise de votre bateau "))
    d=sqrt((a-x)**2+(b-y)**2)
    if d<10:
        print("touché")
    elif d<10:
        print("raté")
        raté+=1
 
print ("il fallait tiré" ,x,y)
raté1=0
for i in range(5):
    p=randint(1,100)
    o=randint(1,100)
    d1=sqrt((p-c)**2+(o-z)**2)
    if d<10:
        print("touché par l'ordi")
    elif d<10:
        print("raté")
        raté1+=1
    
print ("il fallait tiré" ,x,y)
