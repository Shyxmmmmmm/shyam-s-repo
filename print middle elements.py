Input: a = 978, b = 518, c = 300
Output: 518
Explanation: Since 518>300 and 518<978, so 518 is the middle element.

class Solution:
    def middle(self, a, b, c):
        a,b,c=sorted([a,b,c])
        return b

class Solution:
    def middle(self, a, b, c):
        mn=min(a,b,c)
        mx=max(a,b,c)
        
        mid=(a+b+c)-(mn+mx)
        return mid
        
        

#User function Template for python3


        
        
        
