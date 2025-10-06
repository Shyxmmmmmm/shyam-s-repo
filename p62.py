Input: a = "3", b = "10"
Output: 9
Explanation: 310 = 59049. Last digit is 9.

class Solution:
    def getLastDigit(self, a, b):
        return pow(int(a),int(b),10)
