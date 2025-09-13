import sys 

def fac(N):
    res = 1
    for i in range(1,N+1):
        res = res * i
    return res

n = int(sys.stdin.readline())
n_fac = fac(n)
cnt = 0 
while(n_fac != 0):
    if(n_fac % 10 == 0):
        cnt = cnt + 1
        n_fac = n_fac // 10
    else:
        break
print(cnt)