Input: arr[] = [0, -1, 2, -3, 1]
Output: true
Explanation: The triplet [0, -1, 1] has a sum equal to zero.


class Solution:
    def findTriplets(self, arr):
        n=len(arr)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        return True
        return False
