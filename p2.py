3 2 1
3 2
3

class Solution:
    def p(self,N):
        for i in range(1,N+1):
            val=N  #remember val is a temp variable to store the N value.coz if you directly run the N value means it'll works for first [i=1] only "coz the N value is already 0"(so store the N value in temp before assing the row loop)
            for j in range(1,val-i+2):
                print(val,end=" ")
                val=val-1
            print()

sol=Solution()
N=int(input("Input:"))

sol.p(N)
