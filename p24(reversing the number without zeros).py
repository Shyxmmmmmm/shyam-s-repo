Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.



class Solution:
	def reverseDigits(self, n):
	    q=[]
	    while n>0:
	        p=n%10
	        n=n//10
	        q.append(p)
	        
	    s=''   ## ithula naa first [] thaan use panni pathom ana list use panna loop kullla thaan print statement vanganum so it is not convinent one athan na s='' string ahh vangitu atha print pannama retrun pannikalam 
	    for i in q:
	        if i!=0:
	            s=s+str(i)
	    return s
