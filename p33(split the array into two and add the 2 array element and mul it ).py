split the array into two and add the 2 array element and mul it 

ip->n=5 arr=[1,2,3,4,5]

op-> a1=[1,2] a2=[3,4,5]
a1=1+2=3
a2=3+4+5=12
print(a1*a2)



class Solution:
    def p(self,n,arr):
        half=len(arr)//2
        
        a1,a2=arr[:half],arr[half:]
        print(a1,a2)
        c=0
        for i in range(len(a1)):
            c=c+a1[i]
        print(c)
        
        v=0
        for i in range(len(a2)):
            v=v+a2[i]
        print(v)
        
        print(v*c)
        

sol=Solution()
n=int(input())
arr=list(map(int,input().split()))
sol.p(n,arr)
