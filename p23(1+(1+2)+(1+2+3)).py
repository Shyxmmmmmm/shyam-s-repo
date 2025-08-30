sum of all 'n' natural numbers 



class Solution:
    def sumOfTheSeries (self, n):
        s=0
        c=0
        for i in range(1,n+1):
            s=s+i
            c=s+c
        return c



def p():
    n=5
    s=0
    for i in range(1,n+1):
        p=i*(i+1)//2
        s=s+p
    print(s)
    
        
p()

it is important one

def p():
    n=5
    print(n*(n+1)*(n+2)//6)
p()
