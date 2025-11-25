Single Among Doubles in a Sorted



Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.


Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6



class Solution:
    def single(self, arr):
         
        
        for i in range(0,len(arr)):
            if len(arr)==1:
                return arr[i]
            
            if i==0:
                if arr[i]!=arr[i+1]:
                    return arr[i]
            
            elif i==len(arr)-1:
                if arr[i]!=arr[i-1]:
                    return arr[i]
            
            else:
                if arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
                    return arr[i]
                



class Solution:
    def single(self, arr):
        n=len(arr)
        
        if n==1:
            return arr[0] 
        if arr[0]!=arr[0+1]:
            return arr[0] 
        
        if arr[n-1]!=arr[n-2]:
            return arr[-1] 
        
        low=1
        high=n-2
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
                return arr[mid]
            elif arr[mid]==arr[mid-1]:
                low=mid+1
            else:
                high=mid-1
                
        
