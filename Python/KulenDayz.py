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

def podijeli_listu(lista):
    polovina = len(lista)/2
    return lista[:polovina], lista[polovina:]


def ljubav(osoba1,osoba2,log=False):
    
    print(osoba1,osoba2) if log else log
    
    if len(osoba1)<=len(osoba2):
        podaci = osoba1.lower()+osoba2.lower()
    else:
        podaci = osoba2.lower()+osoba1.lower()
    brojevi=list()
    for i in podaci:
        brojevi.append(podaci.count(i))
        
    postotak=0
    while True:
        
        print(brojevi) if log else log
        # s znakon \ prelomio u novi red
        lijevo,desno=brojevi[:int(len(brojevi)/2)], \
                      brojevi[int(len(brojevi)/2):]
        neparni_clan=0
        if len(lijevo)!=len(desno) and len(desno) % 2 == 0:
            neparni_clan=desno[0]
            del(desno[0])

        #print(lijevo,desno,neparni_clan) if log else log
        
        del brojevi[:]
        for i in range(0,len(lijevo)):
            brojevi+=list(map(int, list(str(lijevo[i]+desno[len(desno)-i-1])))) #zbog brojeva koji imaju više od jedne znamenke
        if neparni_clan != 0:
            brojevi.append(neparni_clan)
        if len(brojevi) <= 2 :
            postotak=int("".join(str(i) for i in brojevi))
            break;

    print(brojevi) if log else log
        
    return postotak;
    
def ljubav_znakovno_sucelje(osoba1,osoba2,log=False):
    return osoba1 + " i " + osoba2 + " se vole " + str(ljubav(osoba1,osoba2,log)) + " %"




