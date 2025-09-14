n = 5 arr[] = [1, 2, 3, 5]

Output Format: 4


class Solution:
    def p(self,a,b):
        sum=0
        for i in range(1,a+1):
            sum=sum+i
        
        sum2=0
        for i in range(len(b)):
            sum2=sum2+b[i]
        
        total=sum-sum2
        print(total)
            
                

sol=Solution()
a=int(input())
b=list(map(int,input().split()))
sol.p(a,b)
