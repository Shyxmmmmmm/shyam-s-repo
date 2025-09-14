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
