BINARY SEARCH

first occurse and last occurence

Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output: [2, 5]
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5


Input: arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
Output: [6, 6]
Explanation: First and last occurrence of 7 is at index 6


Input: arr[] = [1, 2, 3], x = 4
Output: [-1, -1]
Explanation: No occurrence of 4 in the array, so, output is [-1, -1]

#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        first=-1
        last=-1
        
        for i in range(0,len(arr)):
            if arr[i]==x:
                if first==-1:
                    first=i
                    last=i
                else:
                    last=i
        return [first,last]



optimized-> USING BINARY SEARCH



#User function Template for python3


class Solution:
    def find(self, arr, x):
        first=self.First(arr,x)
        last=self.Last(arr,x)
        
        return [first,last]
    
    def First(self,arr,x):
        low=0
        high=len(arr)-1
        
        res=-1
        while (low<=high):
            mid=(low+high)//2
            
            if arr[mid]==x:
                res=mid
                high=mid-1
            elif arr[mid]>x:
                high=mid-1
            else:
                low=mid+1
        
        return res
            
    def Last(self,arr,x):
        low=0
        high=len(arr)-1
        
        res=-1
        
        while(low<=high):
            
            mid=(low+high)//2
            
            if arr[mid]==x:
                res=mid
                low=mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return res
        
