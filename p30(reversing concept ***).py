Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.

Input : n = 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.



class Solution:
	def reverseDigits(self, n):
	    q=[]
	    while n>0:
	        p=n%10
	        n=n//10
	        q.append(p)
	        
	    s=''   
	    for i in q:
	        if i!=0:
	            s=s+str(i)
	    return s
