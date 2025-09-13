import sys

list = []

n = int(sys.stdin.readline())
for i in range(1,n+1):
    cor = input()
    a = cor.split(' ')
    tup = (int(a[0]),int(a[1]))
    list.append(tup)

list.sort(key=lambda x: (x[1],x[0]))

for i in list:
    print(i[0],i[1])