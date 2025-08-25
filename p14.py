Input : 325345
Expected output:543523

def p():
    n=int(input())
    while n>0:
        l=n%10
        n=n//10
        print(l,end='')
p()

**************
def p():
    n=123456
    p=0
    while n>0:
        l=n%10
        p=p*10+l
        n=n//10
    
    print(p)
p()

