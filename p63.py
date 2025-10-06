Input: n = 2446
Output: 1
Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

Input: n = 23
Output: 0
Explanation: 2 and 3, none of them divide 23 evenly.

class Solution:
    def evenlyDivides(self, n):
        q=n
        a=[]
        while q>0:
            p=q%10
            a.append(p)
            q=q//10
        
        count=0
        for i in a:
            if  i!=0 and n%i==0  :
                count=count+1
        return count
