ime = input("Unesi ime ")
print("Hello " + ime)


print("Hello", ime)

ocjena=5

print("Ocjena učenika %s je %s" % (ime, ocjena))
print("Ocjena učenika %(u)s je %(o)s" % {"u": ime, "o": ocjena})
print("Ocjena učenika {} je {}".format(ime, ocjena))
print("Ocjena učenika {0} je {1}".format(ime, ocjena))
print("Ocjena učenika {u} je {o}".format(u=ime, o=ocjena))
print("Ocjena učenika",ime,"je",ocjena)
