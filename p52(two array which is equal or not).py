Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]


class Solution:
    def checkEqual(self, a, b) -> bool:
        a1=sorted(a)
        b1=sorted(b)
        
        if a1==b1:
            return True
        else:
            return False

**effetive one

from collections import Counter


class Solution:
    def checkEqual(self, a, b) -> bool:
        if Counter(a) == Counter(b):
            return True
        else:
            return False
sol=Solution()        
a=[1,2,3,4,5]
b=[2,3,4,5]
print(sol.checkEqual(a, b))
