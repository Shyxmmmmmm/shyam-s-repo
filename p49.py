Aloka is stuck in an island, she has a solve a problem to get out of the island. You are given n numbers in sorted order, you need to find the first and last occurrence of the number x and print them. If occurrence of a number is not found, then print -1.

Input Format

n = 8 arr ={2,3,4,4,4,5,5,6} x = 4


Output Format

2 4


class Solution:
    def p(a,b,c):
        first=-1
        last=-1
        for i in range(len(b)):
            if b[i]==c:
                if first==-1:
                    first=i
                last=i
        
        if first==-1:
            print(-1)
        else:
            print(first)
            print(last)
        

sol=Solution
a=int(input())
b=list(map(int,input().split()))
c=int(input())
sol.p(a,b,c)
