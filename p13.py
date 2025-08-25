Input: a = 3, b = 3, k = 1
Output: 7
Explanation: 33 = 27 and 1st digit from right is 7


class Solution():
    def kthDigit(self, a, b, k):
        c=a**b
        p=[]
        while(c>0):
            l=c%10
            p.append(l)
            c=c//10
            
            
        count=0
        for i in p:
            count=count+1
            if count==k:
                return i
            
