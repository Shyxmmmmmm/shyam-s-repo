1
23
456


class Solution:
    def p(self,n):
        num=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(num,end=' ')
                num=num+1
            print()
       
            
    
sol=Solution()
sol.p(5)
            


what if in the question they said to stop num==10:




class Solution:
    def p(self,n):
        num=1
        stop=False
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(num,end=' ')
                if num==10:
                    stop=True
                    break
                num=num+1
            print()
            if stop:
                break
            
    
sol=Solution()
sol.p(5)

            
