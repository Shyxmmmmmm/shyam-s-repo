class Solution:
    def p(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end='')
            print()
sol=Solution()
sol.p(5)