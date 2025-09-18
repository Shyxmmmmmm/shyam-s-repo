FIRST DUPLICATE ELEMENT

arr=[1,2,3,4,5,6,4]
n=len(arr)
a=[]
b=[]
for i in range(0,n):
    if arr[i] not in a:
        a.append(arr[i])
    else:
        b.append(arr[i])
print(b)
