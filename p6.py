class Solution:
    def p(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+1):
                print(" ",end='')
            
            for k in range(1,i*2):
                print("*",end="")
            
            print()
        
        for i in range(1,n):
            for j in range(1,i+1):
                print(" ",end="")
            
            for k in range(1,n-(2*i)+4):
                print("*",end='')
            print()
    
sol=Solution()
sol.p(4)

