Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

class Solution:
    def frequencyCount(self, arr):
        a=[]
        for i in range(1,len(arr)+1):
            b=arr.count(i)
            a.append(b)
        return a

