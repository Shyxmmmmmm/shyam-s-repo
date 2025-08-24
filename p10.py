#count of numbers
n=12345
count=5

class solution:
    def p(self,n):
        count=0
        while(n>0):
            n=n//10
            count=count+1
        print(count)
sol=solution()
n=int(input())

sol.p(n)



