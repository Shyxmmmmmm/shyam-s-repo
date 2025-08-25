Input: N = 12345
Output: 6
Explanation: 1st and last digits are 1 and 5.


#User function Template for python3

class Solution:
	def corner_digitSum(self, n):
	    ld=n%10
	    while(n>0):
	        Fr=n%10
	        n=n//10
	        if n==0:
	            return Fr+ld
	        
