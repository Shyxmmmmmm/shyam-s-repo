#perfect Number

def p():
    n=int(input("Enter the Number:"))
    q=[]
    for i in range(1,n):
        if n%i==0:
            q.append(i)
    print(q)
    
    s=0
    for i in q:
        s=s+i
    if s==n:
        print("it is perfect number")
    else:
        print("it is not perfect Number")
p()
