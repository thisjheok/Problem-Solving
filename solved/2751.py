import sys

numbers = []
T = int(sys.stdin.readline())
for i in range(T):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])