n=15
op----> 2,3,5,7,11,13


def p():
    n=15
    for i in range(2,n+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                
        if flag==0:
            print(i,end=' ')
p()
