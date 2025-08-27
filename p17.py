prime or not prime

def p():
    n=10
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
        
    if flag==0:
        print("Not Prime")
    else:
        print("Prime")
            
p()
