Input: arr[] = [10, 8, 30, 4, 5], x = 5
Output: 4
Explanation: For array [10, 8, 30, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.



Input: arr[] = [10, 8, 30], x = 6
Output: -1
Explanation: The element to be searched is 6 and it is not present, so we return -1.



class Solution:
    def search(self, arr, x):
        flag=0
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1

                
