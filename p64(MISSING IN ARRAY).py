Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.



class Solution:
    def missingNum(self, arr):
        a=sorted(arr)
        b=a[-1]
        if len(a)==1:
            if a[0]!=1:
                return 1
            return 2
        c=[]
        for i in range(1,b+1):
            c.append(i)
            
        for i in range(0,b):
            if a[i]!=c[i]:
                return c[i]
        return b+1
                
