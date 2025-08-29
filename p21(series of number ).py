series of number 
1,3,6,10,15,21

1+3+6+10+15+21=35


def p():
    n=int(input("Enter the ip:"))
    p=0
    s=0
    q=[]
    for i in range(1,n+1):
        p=p+i
        s=s+p
    print(s)
p()
