print the zeros at the last


class Solution:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    j=0
	    for i in range(0,n):
	        if arr[i]!=0:
	            arr[j]=arr[i]
	            j=j+1
	    
	    for i in range(j,n):
	        arr[i]=0
	    return arr

optimized:

class Solution:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    j=0
	    for i in range(0,n):
	        if arr[i]!=0:
	            arr[i],arr[j]=arr[j],arr[i]
	            j=j+1
	   return arr
	            
