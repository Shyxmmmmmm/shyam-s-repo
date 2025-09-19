PALINDROME


a='naan'
j=''
n=len(a)
for i in range(n-1,-1,-1):
    j=j+a[i]
if a==j:
    print(True)
else:
    print(False)




def p():
    a='naaan'
    n=len(a)
    j=n-1
    i=0
    while(i<j):
        if a[i]!=a[j]:
            return False
        j=j-1
        i+=1
    return True
print(p())

    
        
        
