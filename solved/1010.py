def factorial(n):
    if(n>1):
        return n * factorial(n-1)
    else: 
        return 1

def combination(n,r):
    n_fac = factorial(n)
    r_fac = factorial(r)
    n_r_fac = factorial(n-r)
    
    return n_fac/(r_fac * n_r_fac)

T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    print(int(combination(m,n)))