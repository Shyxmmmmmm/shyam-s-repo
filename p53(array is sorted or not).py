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

simple linear search:it is effective one:

class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True


