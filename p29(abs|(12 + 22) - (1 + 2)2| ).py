Input: N = 2
Output: 4 
Explanation: abs|(12 + 22) - (1 + 2)2| = 4.


import math
#User function Template for python3
class Solution:
    def squaresDiff (self, N):
        for i in range(1,N+1):
            a=N*(N+1)//2
            b=N*(N+1)*((2*N)+1)//6
            c=(b-a**2)
            return abs(c)
            
