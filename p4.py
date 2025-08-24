*
**
***
**
*


class Solution:
    def p(self,N):
        for i in range(1,2*N):
            if i<=N:
                start=i
            else:
                start=2*N-i
            for j in range(1,start+1):
                print("*",end='')
            print()
        



sol=Solution()
m=int(input("Input:"))

sol.p(m)


#time complixity matters 

class Solution:
    def p(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
            
        for i in range(1,N):
            for j in range(1,N+1-i):
                print("*",end='')
            print()

sol=Solution()
m=int(input("Input:"))
sol.p(m)

