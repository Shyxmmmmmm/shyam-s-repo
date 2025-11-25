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
                
        
        
