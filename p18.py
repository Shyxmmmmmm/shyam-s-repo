prob statement:
ip-> n=7
op-> 1,2,3,5,7



def p():
    n=5
    q=[]
    for i in range(1,n+1):
        if i%2!=0:
            print(i,end=" ")
            q.append(i)
    print()
    print(q)
            
        
p()
