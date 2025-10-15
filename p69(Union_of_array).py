Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.


class Solution:    
    def findUnion(self, a, b):
        a1=sorted(set(a))
        b1=sorted(set(b))
        c=a1+b1
        d=sorted(set(c))
        return d
        
