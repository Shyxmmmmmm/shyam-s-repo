Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.


Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.



class Solution:
    def rotate(self, arr):
        n=len(arr)
        temp=arr[n-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        
        return arr
    
