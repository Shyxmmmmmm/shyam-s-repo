Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.



class Solution:
    def isSorted(self, arr) -> bool:
        a=sorted(arr)
        if arr==a:
            return True
        else:
            return False
