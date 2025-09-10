RECURSION PRINTING elements in array


def p(a,n,i):
    if i>=n:
        return
    else:
        print(a[i],end=' ')
        return p(a,n,i+1)
def main():
    a=[1,23,4,5,6]
    n=5
    i=0
    p(a,n,i)
    
main()
