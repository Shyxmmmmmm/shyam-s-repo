Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10

Input: n = 5
Output: 1 2 3 4 5

Input: n = 1
Output: 1


class Solution:    
    def printNos(self,n):
        if n==0:
            return 0
        
        else:
            self.printNos(n-1)
            print(n,end=' ')
