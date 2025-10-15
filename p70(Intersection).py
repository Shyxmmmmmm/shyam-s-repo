Input: a[] = [89, 24, 75, 11, 23], b[] = [89, 2, 4]
Output: 1
Explanation: 89 is the only element in the intersection of two arrays.


class Solution:
    def intersectSize(self,a, b):
        a1=sorted(set(a))
        b1=sorted(set(b))
        count=0
        for i in range(0,len(a1)):
            for j in range(0,len(b1)):
                if a[i]==b[j]:
                    count=count+1
        return count
