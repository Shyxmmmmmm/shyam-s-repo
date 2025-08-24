  *
 ***
*****
*****
 ***
  *


def p():
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(1,i*2):
            print("*",end="")
        print()
        
    for i in range(1,n+1):
        for j in range(1,i-n+3):
            print(" ",end="")
        for k in range(1,(n*2)-(i*2)+2):
            print("*",end="")
        print()
p()
