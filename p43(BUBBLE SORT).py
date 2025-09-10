BUBBLE SORT


a=[9,11,3,2,10]
n=len(a)
for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j+1]<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)
    
        
