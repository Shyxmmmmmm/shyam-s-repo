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