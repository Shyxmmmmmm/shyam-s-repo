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
