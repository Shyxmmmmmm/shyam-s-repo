Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.

Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.


#User function Template for python3
class Solution:
	def arraySum(self, arr):
	    sum=0
	    for i in arr:
	        sum=sum+i
	    return sum
