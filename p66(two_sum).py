Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: arr[3] + arr[4] = -3 + 1 = -2

class Solution:
	def twoSum(self, arr, target):
		n=len(arr)
		if n==1 :
		    return False
		for i in range(0,n):
		    for j in range(i+1,n):
		        if arr[i]+arr[j]==target:
		            return True
		return False
