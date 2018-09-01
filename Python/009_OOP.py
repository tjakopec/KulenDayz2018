#
# KLASA
#
class Kulen:
    proizvođač=""
    organoleptičkaSvojstva=0
    fizikalnoKemijskaAnaliza=0
    __privatno_svojstvo=""

    """
        What do you mean by "fighting the language"?

        Guido: That usually means that they're trying to continue their habits that worked well with a different language.

        [...] People will turn everything into a class, and turn every access into an accessor method,
        where that is really not a wise thing to do in Python; you'll have more verbose code that is
        harder to debug and runs a lot slower. You know the expression "You can write FORTRAN in any language?" You can write Java in any language, too.
    """


    def __init__(self,
                 proizvođač="",
                 organoleptičkaSvojstva=0,
                 fizikalnoKemijskaAnaliza=0):
        self.proizvođač=proizvođač
        self.organoleptičkaSvojstva=organoleptičkaSvojstva
        self.fizikalnoKemijskaAnaliza=fizikalnoKemijskaAnaliza

    def ukupno(self):
        if self.proizvođač == "Mata":
            return 81
        else:
            return self.fizikalnoKemijskaAnaliza * self.fizikalnoKemijskaAnaliza
    

kuleni=list()

#
# OBJEKT
#
k= Kulen()
k.proizvođač="Stipe"
k.organoleptičkaSvojstva=9
k.fizikalnoKemijskaAnaliza=7
kuleni.insert(0,k)

kuleni.insert(0,Kulen("Mata",7,3))
ukupno=0
for i in kuleni:
    print(i.proizvođač, i.ukupno())
    ukupno+=i.ukupno()

print("prosjek", ukupno/len(kuleni))


#
# Nasljeđivanje -> VIŠESTRUKO :)
#

class Osoba:
    ime=""
    prezime=""


class Student:
    jmbag=""


class Brucos(Osoba,Student):
    bioNaBrucosijadi=False

    #magija :) https://rszalski.github.io/magicmethods/
    def __str__(self):
        return self.ime + " " + self.prezime + " " + ("je" if self.bioNaBrucosijadi else "nije") + " bio na brusošijadi"


s=Brucos()

s.ime="Ivica"
s.prezime="Kičmanović"
s.jmbag="012327282732"
s.bioNaBrucosijadi=True

print(s)

#Više čitanja na
#https://pythonspot.com/encapsulation/
#https://pythonspot.com/polymorphism/
#https://docs.python.org/3/tutorial/classes.html
#https://realpython.com/python3-object-oriented-programming/

