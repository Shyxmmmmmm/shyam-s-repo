ROTATION OF STRING


class Solution(object):
    def rotateString(self, s, goal):
        n=len(s)
        for i in range(0,n):
            arr=s[i:]+s[:i]
            if arr==goal:
                return True
        return False
        
