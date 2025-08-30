1,3,6,10,15,21

print N'th number:

class Solution:
    def findNthTerm(self, n):
        return n*(n+1)//2
        

#User function Template for python3

class Solution:
    def findNthTerm(self, n):
        s=0
        for i in range(1,n+1):
            s=s+i
        return s
        
