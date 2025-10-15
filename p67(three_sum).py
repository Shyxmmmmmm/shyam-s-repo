Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true 
Explanation: The triplet {1, 4, 8} sums up to 13.


class Solution:
    def hasTripletSum(self, arr, target):
        n=len(arr)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==target:
                        return True
        return False
        
