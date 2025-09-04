Input: key = 2 , arr = [10, 20, 30, 40, 50]
Output: 30
Explanation: The value of arr[2] is 30 .



Input: key = 4 , arr = [10, 20, 30, 40, 50, 60, 70]
Output: 50
Explanation: The value of the arr[4] is 50 .


from typing import List


class Solution:
    def findElementAtIndex(self, key : int, arr : List[int]) -> int:
        for i in range(len(arr)):
            if i==key:
                return arr[i]
