REVERSING THE STRING

a='shyam'
n=len(a)
a=list(a)
j=0
for i in range(n-1,-1,-1):
    if i==j:
        break
    else:
        a[i],a[j]=a[j],a[i]
        j=j+1
a=''.join(a)
print(a)
        
