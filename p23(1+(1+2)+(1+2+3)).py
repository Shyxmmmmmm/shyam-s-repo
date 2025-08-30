sum of all 'n' natural numbers 



class Solution:
    def sumOfTheSeries (self, n):
        s=0
        c=0
        for i in range(1,n+1):
            s=s+i
            c=s+c
        return c
