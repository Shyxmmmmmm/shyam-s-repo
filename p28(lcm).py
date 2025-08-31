lcm of two numbers:


import math
class Solution:
    def p(self,a,b):
        l=abs(a*b)//math.gcd(a,b)
        print(l)
sol=Solution()
a,b=map(int,input().split())
sol.p(a,b)

for GCD:


class Solution:
    def gcd(self, a, b):
        while b!=0:
            a,b=b,a%b
        return a
