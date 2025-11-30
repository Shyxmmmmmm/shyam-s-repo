nput: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.


Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.


class Solution:
    def intersect(self, a, b):
        a.sort()
        b.sort()
        
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                if (len(res)==0 or res[-1]!=a[i]):
                    res.append(a[i])
                i=i+1
                j=j+1
            elif a[i]>b[j]:
                j=j+1
            else:
                i=i+1
        return res
