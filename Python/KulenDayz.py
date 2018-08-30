def prostiBroj(x):
    for i in range(2,x-1):
        if x % i == 0: return False 
    return True

def prostiBrojevi(od,do):
    brojevi=list()
    for i in range(od,do):
        if prostiBroj(i):
            brojevi.insert(0,i)
    return sorted(brojevi)

def zbrojProstihBrojeva(od,do):
    x=0
    for i in prostiBrojevi(od,do):
        x+=i
    return x

def brojZnamenkiZbrojaProstihBrojeva(od,do):
    x=zbrojProstihBrojeva(od,do)
    return len(str(x))
