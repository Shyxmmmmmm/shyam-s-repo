sum of all number using recursion 



def p(n):
    if n==0:
        return 0
    else:
        return (n%10)+p(n//10)

def main():
    print(p(123456))
main()
