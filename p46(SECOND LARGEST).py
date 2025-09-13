SECOND LARGEST


class Solution:
    def getSecondLargest(self, arr):
        a=-1
        n=len(arr)
        for i in range(0,n):
            if a<arr[i]:
                a=arr[i]
        
        b=-1
        for i in range(0,n):
            if b<arr[i] and arr[i]!=a:
                b=arr[i]
        return b
