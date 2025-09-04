Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: [-1]
Explanation: Only element is 1 which is smallest, so there is no second smallest element



class Solution:
    def minAnd2ndMin(self, arr):
        s=sorted(set(arr))
        if len(s)<2:
            return [-1]
        a,b=s[0],s[1]
        return [a,b]
            
