class Solution:
    def p(self,n):
        for i in range(1,n+1):
            for j in range(1,i):
                print(" ",end='')
            
            for k in range(1,n*2-(2*i)+2):
                print("*",end="")
            print()
sol=Solution()
sol.p(5)