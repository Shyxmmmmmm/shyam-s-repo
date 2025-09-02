Reversing concept important advise:

def p():
    n=12345
    while n>0:
        p=n%10
        print(p,end=' ')
        n=n//10
p()
## ithuvum reversing thaan ana intha method ah vachi namma oru oru int ah thaaan print panna mudiyum like if u want to print n=54321 it is not possible in this method



def p():
    n=12345
    s=0
    while n>0:
        p=n%10
        s=10*s+p
        n=n//10
    print(s)
p()
## learn this method ok because it is efficient than above one 
