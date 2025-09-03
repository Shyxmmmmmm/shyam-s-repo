Finding largest value in array


a=[1231,2,345,567,2]
l=a[0]
for i in range(len(a)):
    if l<a[i]:
        l=a[i]
print(l)
