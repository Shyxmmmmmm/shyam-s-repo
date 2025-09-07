Input: n = 5
Output: 5
Explanation: The 5th Fibonacci number is 5.


Input: n = 0
Output: 0 
Explanation: The 0th Fibonacci number is 0.


Input: n = 1
Output: 1
Explanation: The 1st Fibonacci number is 1.



class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
            
        
