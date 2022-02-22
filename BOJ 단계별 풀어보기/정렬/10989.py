# 10989. 수 정렬하기 3
import sys

numbers = dict()
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    numbers[n] = numbers.get(n,0) +1

numbers = sorted(numbers.items() , key= lambda x : x[0])

for x in numbers:
    for _ in range(x[1]):
        print(x[0])