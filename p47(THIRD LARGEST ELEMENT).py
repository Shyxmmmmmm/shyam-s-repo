THIRD LARGEST ELEMENT:


class Solution:
    def thirdLargest(self,arr):
        n=len(arr)
        a=-1
        for i in range(0,n):
            if a<arr[i]:
                a=arr[i]
                
        b=-1
        for i in range(0,n):
            if b<arr[i] and arr[i]!=a:
                b=arr[i]
        
        c=-1
        for i in range(0,n):
            if c<arr[i] and arr[i]!=a and arr[i]!=b:
                c=arr[i]
        return c
