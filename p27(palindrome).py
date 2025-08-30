class Solution:
    def isPalindrome(self, n):
        h=n
        s=0
        while n>0:
            p=n%10
            s=s*10+p
            n=n//10
        if s==h:
            return True
        else:
            return False
