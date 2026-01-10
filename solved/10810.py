m,n = map(int, input().split())
arr = []

for i in range(m):
    arr.append(0)

for _ in range(n):
    a,b,c = map(int, input().split())
    for i in range(a-1,b):
            arr[i] = c


print(*arr)