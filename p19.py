ip-> 6
op->2 [explanation 6->divisors 1,2,3,6 which are divided by 3 ->[3,6]---so the final answer is 2]


#User function Template for python3

class Solution:
    def countDivisors(self, n):
        q=[]
        for i in range(1,n+1):
            if n%i==0:
                q.append(i)
        
        count=0
        for i in q:
            if i%3==0:
                count=count+1
        return count 
                
