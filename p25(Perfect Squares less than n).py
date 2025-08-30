Input: n = 9
Output: 2
Explanation: 1 and 4 are the only Perfect Squares less than 9. So, the Output is 2.

import math
class Solution:
    def countSquares(self, n):
        s=int(math.sqrt(n-1))
        return s
