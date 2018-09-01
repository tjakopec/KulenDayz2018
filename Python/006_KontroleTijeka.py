#
# IF
#
x = 2 # preporuka je stavljati razmake prije i nakon operatora. Autor naučio da to radi IDE a IDLE to nema :(

if x == 2:
    print("broj je 2")

#radi s boolean tipom podatka
provjera = x == 2
print(type(provjera))

if provjera:
    print("broj je 2")
 

x="2"

if x==2:
    print('Broj je "2"')
else:
    print('Broj nije "2"')

# Python nema &, samo &&
def a():
    print("Provjeravam AAAAAA")
    return False

def b():
    print("Provjaravam BBBBBB")
    return True

if a() and b():
    print("OK")


# if in
lista = (1,2,2,3,4,2,3,2)
x = 4
if x in lista:
    print("in")


#
# ELIF
#

#nema swith-a !?!?!?
    #ali ima elif

x=5;

if x==1:
    print("Nedodvoljan")
elif x==2:
    print("Dovoljan")
elif x==3:
    print("Dobar")
elif x==4:
    print("Vrlo dobar")
elif x==5:
    print("Odličan")
else:
    print("Broj nije ocjena")
    
#inline if

x=2

print("Super" if x==5 else "Moglo je bolje")



#
# PETLJE
#


# for
#iteracija 0 do 9 za 1
for i in range(10):
    print(i, end = " ")
print()
#iteracija 0 do 9 za 1
for i in range(0,10):
    print(i, end = " ")
print()
#iteracija 0 do 9 za 2
for i in range(0,10,2):
    print(i, end = " ")
print()
#iteracija 10 do 1 za 1
for i in range(10,0,-1):
    print(i, end = " ")
print()

#iteracija 10 do 0 za 1
for i in range(10,-1,-1):
    print(i, end = " ")
print()

#preskakanje petlje
for i in range(10):
    if i==2:
        continue
    print(i, end = " ")
print()
#nasilno prekidanje petlje
for i in range(10):
    if i==2:
        break
    print(i, end = " ")
print()

#while
# uvijek radi s boolean tipom podatka
#beskonačna petlja
#while True:
#    print("Hello")
i=0
while i<10:
    print(i, end = " ")
    i+=1
print()

# continue i break djeluju jednako i u while


#
# Ugnježđivanje petlji
#

"""
from random import *
while True:
    for i in range(randrange(1,100)):
        if i==1:
            print("Marija, sviđaš mi se!", end=" ")
        print(random(), end=" ")
"""

#iteracija strukturi podataka

lista=[7,7.5,7+2j, "Niz znakova", bool(1)]
for e in lista:
    print(e)

lista=(7,7.5,7+2j, "Niz znakova", bool(1))

for e in lista:
    print(e)

lista={1,7,7,5,5,5,2,2,2,2}

for e in lista:
    print(e)


x="KulenDayz"
for e in x: print(e, end=" ❤ ") #http://graphemica.com/unicode/characters


# NE MOŽE
#x=2227373
#for e in x:
#    print(e)
