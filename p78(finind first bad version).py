Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


[its like first occurence]


class Solution(object):
    def firstBadVersion(self, n):
        i=0
        j=n

        ans=-1

        while i<=j:
            mid=(i+j)//2

            if isBadVersion(mid):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
