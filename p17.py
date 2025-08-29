prime or not prime

import math

class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                return False
        return True



class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        flag=0
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        
        if flag==1:
            return False 
        else:
            return True






def p():
    n=10
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
        
    if flag==0:
        print("Not Prime")
    else:
        print("Prime")
            
p()
