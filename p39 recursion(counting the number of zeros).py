counting the number of zeros in the given number>
ip->1230
op->1

ip->001230
op->3



def p(n):
    if n%10==n:
        if n==0:
            return 1
        else:
            return 0
    
    if n%10==0:
        return 1+p(n//10)
    else:
        return p(n//10)

def main():
    print("there are",p(2000030),"Zeros in this number")
main()
