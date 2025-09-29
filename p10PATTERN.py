1
01
101
0101
10101



n=5
for i in range(1,n+1):
    for j in range(0,i):
        sum=i+j
        if sum%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print()
