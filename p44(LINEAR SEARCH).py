LINEAR SEARCH:


def p(a,n,i,t):
    if i>=n:
        return 0
    if a[i]==t:
        return True
    else:
        return p(a,n,i+1,t)
    
    
def main():
    a=[1,24,3,4,25]
    n=5
    i=0
    t=25
    print(p(a,n,i,t))
    
main()
