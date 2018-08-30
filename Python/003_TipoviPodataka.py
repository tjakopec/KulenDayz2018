#komentar jedna linija
"""
Komentar više
linija
"""


"""
BROJEVI
"""
#cijeli broj
x = 7
print(x, "=>", type(x))

#decimalni broj
x = 7.5
print(x, "=>", type(x))

#kompleksni broj
x = 7+2j
print(x, "=>", isinstance(1+2j,complex), "Kompleksni broj")



"""
LISTE
"""
#
# list
#
# elementi liste mogu biti kombiniranih tipova podataka
lista=[7,7.5,7+2j, "Niz znakova", bool(1)]
print(lista)

#djelovi liste
x = [1,2,3,4,5,6,7,8,9]
print("x[2] = ", x[2])
print("x[0:3] = ", x[0:3])
print("x[5:] = ", x[5:])

#dodaj element na index 0, svi ostali indeksi se pomjere
x.insert(0,-1)
print(x)
# briši zadnji element liste
del x[len(x)-1]
print(x)

# lista se mogu mjenjati (mutable)
x[2]=7
print(x)

#
# tuple
#
# jednako kao lista uz iznimku što se elementi liste ne mogu mijenjati (immutable)
lista=(7,7.5,7+2j, "Niz znakova", bool(1))
print(lista)

#djelovi liste
x = (1,2,3,4,5,6,7,8,9)
print(x)
print("x[2] = ", x[2])
print("x[0:3] = ", x[0:3])
print("x[5:] = ", x[5:])
# tuple se ne može mjenjati (TypeError: 'tuple' object does not support item assignment)
#x[2]=7
#print(x)


#
# set
#
# jednako kao lista uz iznimku što se elementi mogu biti jedinstveni

x = {1,7,7,5,5,5,2,2,2,2}
print(x)
x=sorted(x, reverse=True)
print(x)
x.insert(0,3)
print(x)
x=sorted(x)
print(x)


#
# dictionary (json look-alike)
#
x={"ime":"Tomislav","godine": 38}
print(x)
print(x["ime"])

#
# kombiniram (kao Praskaton)
#
x=1
podaci = {
    "sifra": x,
    "ocjene": (2,2,3,2,3,2,3,2,3,2),
    "bodovi": [7,8,7,6,5,6,7,6,5,6],
    "stavke": {1,2,3,4,5,6,7,8,9,10}
    }
print(podaci)

#
# ZNAKOVNI (String)
#

x="KulenDayz"
print(x)
print(x[0])   
print(x[2:5])
print(x[2:])    
print(x * 2)
print(x + " 2018") # Prints concatenated string

#stringovi se ne mogu mjenjati (immutable)
#x[2]="B"
x=list(x)
x[2]="B"
x="".join(x)
print(id(x))
print(x)
x=x.replace("B","l")
print(id(x))
print(x)

#
# konverzije
#

x=float("58.8")
print(x)
x=int(x)
print(x)
string=str(x)
print(string)
lista=list(string)
print(lista)
skup=set(string)
print(skup)
ntorka=tuple(string)
print(ntorka)
rjecnik=dict([("x1",1),("x2",1)])
print(rjecnik)

# daljnje čitanje https://docs.python.org/3/library/functions.html

