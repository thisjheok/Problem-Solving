m,n = map(int, input().split())

def _swap(arr,a,b):
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp


arr = []
for i in range(m):
    arr.append(i+1)

for j in range(n):
    a,b = map(int, input().split())
    _swap(arr,a,b)
    
print(*arr)