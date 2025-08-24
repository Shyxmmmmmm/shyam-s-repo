n=12345
p=[5,4,3,2,1]


class Solution:
    def p(self,n):
        p=[]
        while(n>0):
            l=n%10
            p.append(l)
            n=n//10
        print(p)


sol=Solution()
n=int(input("Enter the input:"))
sol.p(n)
        




class Solution:
    def p(self):
        n=123456
        c=[]
        while (n>0):
            l=n%10
            c.append(l)
            n=n//10
        for i in reversed(c):
            print(i,end=' ')
sol=Solution()

sol.p()

          
