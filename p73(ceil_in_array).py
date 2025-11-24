Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.




#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        low=0
        high=len(arr)-1
        res=len(arr)
        while low<=high:
            
            mid=(low+high)//2
            
            if arr[mid]>=x:
                res=mid
                high=mid-1
            else:
                low=mid+1
        
        if low<len(arr):
            return low
        else:
            return -1
            
