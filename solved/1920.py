import sys
s = set()

n = int(input())
a = input().split()
for i in a:
    s.add(int(i))
    
m = int(input())
b = input().split()
for i in b: 
    if int(i) in s:
        print(1)
    else:
        print(0)
