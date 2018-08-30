def hello():
    print("Hello")


hello()


def hello(tko):
    print("Hello",tko)


hello("Dora")


def parniBroj(x):
    return x % 2 == 0

x=5

print(x, "je" if parniBroj(x) else "nije", "parni broj")


def opcionalniParametri(x,y=1,z="OK"):
    return str(x + y) + ": " + z;

print(opcionalniParametri(1))

print(opcionalniParametri(1,2))

print(opcionalniParametri(1,3,"X"))


import time



start = time.time()

import KulenDayz as k
x=22 #35925949   4666527007
print(x,"je" if k.prostiBroj(x) else "nije", "prosti broj")
# izvođenje
# 4666527007 je prosti broj
# 642.0818817615509 cca 10 min
end = time.time()
print(end - start)


"""
java

long startTime = System.nanoTime();

       long x = 4666527007L;
       boolean prosti=true;
       for(long i=2;i<x-1;i++){
           if(x%i==0){
               prosti=false;
               break;
           }
       }
        System.out.println(x +  (prosti ? " je " : " nije ") + " prosti broj ");
              

     long stopTime = System.nanoTime();
     
     long elapsedTime = stopTime - startTime;
        double seconds = (double)elapsedTime / 1000000000.0;
     
        System.out.println(seconds);

4666527007 je  prosti broj 
40.672085967  !!!!!! sekundi  !!!!


"""
od,do=24,90

for i in k.prostiBrojevi(od,do):
    print(i,end="+")

print("=",k.zbrojProstihBrojeva(od,do))

print(k.brojZnamenkiZbrojaProstihBrojeva(od,do))
