#https://docs.python.org/3/library/math.html
import math #dio osnovne isntalacije
print(math.pi)


#pip => Python Packaging Index => upravitelj instalacijama

# koristeći znakovno sučelje => win: cmd, linux: bash, macOs: terminal
# python -m pip install imePaketa

#primjer instalacije scipy paketa
#pip install scipy

#način 1
#from scipy import constants
#print(constants.pi)

#način 2
import scipy.constants as k
#način 3
#from scipy import constants as k
print(k.pi)

#http://scienceworld.wolfram.com/physics/ThomsonCrossSection.html
print(k.value("Thomson cross section"))

#više na https://docs.scipy.org/doc/scipy/reference/constants.html

# djeci zanimljivo crtanje
import turtle as t
t.fd(100)
