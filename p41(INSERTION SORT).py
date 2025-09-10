INSERTION SORT



a=[5,4,1,21,3]
n=len(a)
for i in range(1,n):
    k=a[i]
    j=i-1
    while j>=0 and k<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=k
print(a)
