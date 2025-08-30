Input: n = 555
Output: true

class Solution:
    def isPalindrome(self, n):
        h=n  ### purinjikoo ipo n ah direct ah use panna while loop laa n ah vachi operation panni mudikum pothu atlast n=0 nu vanthuru so initial ah n ah vera or var la store panni vachikerathu safe 
        s=0
        while n>0:
            p=n%10
            s=s*10+p
            n=n//10
        if s==h:
            return True
        else:
            return False
