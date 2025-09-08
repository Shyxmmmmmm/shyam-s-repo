BUBBLE SORT:


n=10
a=[99,102,2,76,91,11,9,6,19,1]
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
