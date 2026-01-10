arr = []
arr2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
for _ in range(28):
    n = int(input())
    arr.append(n)

arr.sort()
arr3 = list(set(arr2)-set(arr))
arr3.sort()

for i in range(len(arr3)):
    print(arr3[i])
