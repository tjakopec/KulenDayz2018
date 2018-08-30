
# aritmetički operator + - * / % // **

# NEMA ++ --

x=3.8 + 2
print(x)


x=9-3
print(x)

x=3.8 * 2.737363635
print(x)

x=1/3
print(x)

x = 3 % 2
print(x)

x= 1 // 3
print(x)

x= 9 // 2
print(x)

x = 2 ** 3
print(x)


#
# Operatori usporedbe == < > <= => !=
#

x = 2 # dodjeljivanje vrijednosti

if x == 2: print("jednako") #provjera jednakosti
if x > 2: print("veće") # moguće je >=  <=

if not(x > 2): print("manje")

x = 3
if x != 2: print("različito")



#
# Logički operateri and or not
#

x, y = 1, 2 # deklariranje više varijabli u istoj liniji i dodjeljivanje vrijednosti

if x == 1 and y == 2: print("OK")

if x > 0 or y < 10: print("OK")

if not(x != 1 and y != 2): print("OK")


#
# Operatori dodjeljivanja = += -= *= /= %= //= **= &= |= ^= >>= <<=
#

x=2
print(x)
x=x+2
print(x)
x+=2
print(x)


#
# Ostali operatori is | is not | in | not in
#

x=2
y=2
if x is y: print("OK")
if x is not y+1: print("i ovo je OK")
b=[1,1,2,3,4,3,2,2,2]
if 4 in b: print("postoji 4 u b")
if 7 not in b: print("broja 7 nema u b")




#
# Operatori na bitovima [preskočio]
#

# više na https://www.programiz.com/python-programming/operators
