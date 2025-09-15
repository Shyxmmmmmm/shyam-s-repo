Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.



class Solution:
    def sortInWave(self, arr):
        n=len(arr)
        for i in range(0,n-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
        
