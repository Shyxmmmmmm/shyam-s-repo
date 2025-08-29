#problem statement:
#ip:   n=5
#op:   120 with 1 leading zeros

def p():
    n=int(input("Enter the number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    sum=0
    while fact>0:
        shyam=fact%10
        if shyam==0:
            sum=sum+1
        fact=fact//10
    if sum==0:
        print("There is no Leading Zero")
    else:
        print(sum,"leading Zeros")
p()
