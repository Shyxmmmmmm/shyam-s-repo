finding even or odd elements in array


a=[1,2,3,4,5]
even=0
odd=0
for i in range(len(a)):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print(even,odd)
