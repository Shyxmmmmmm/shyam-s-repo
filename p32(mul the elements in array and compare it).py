mul the elements in array and compare it :
if mul of arr1 and mul of arr2 is equal then return 0 ekse return 1



class Solution:
    def p(self,n,arr1,arr2):
        n=1
        for i in range(len(arr1)):
            n=n*i
        print(n)
        
        m=1
        for i in range(len(arr2)):
            m=m*i
        print(m)
        
        if n==m:
            print(1)
        else:
            print(0)
        
sol=Solution()
n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
sol.p(n,arr1,arr2)
        
