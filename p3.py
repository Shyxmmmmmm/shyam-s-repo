class Solution:
    def p(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print('*',end='')
            print()

sol=Solution()
m=int(input("Input:"))
sol.p(m)