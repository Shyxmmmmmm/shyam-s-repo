Search in Rotated Sorted Array

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.


Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.


class Solution:
    def search(self, arr, key):
        low=0
        high=len(arr)-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==key:
                return mid
                
            if arr[low]<=arr[mid]:
                if arr[low]<=key and key<arr[mid]:
                    high=mid-1
                else:
                    low=mid+1
            
            else:
                if arr[mid]<key and key<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
