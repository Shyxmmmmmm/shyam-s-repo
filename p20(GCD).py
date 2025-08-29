gcd of 2 numbers


class Solution:
    def gcd(self, a, b):
        while b!=0:
            a,b=b,a%b
        return a



class Solution:
    def gcd(self, a, b):
        s=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                s=i
        return s
