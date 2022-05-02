# 15649 N과 M (1)

# 입력받기
# 큰 for문 안에 while n < M : 요렇게 진행

# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())

# crit = 0

# answer = list() 
# for _ in M : #for문 개수
#     for x in range(1,N+1): 

# itertools를 사용해야하나 
from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for result in permutations([x for x in range(1,N+1)],M):
    for i in list(result):
        print(i, end=" ")
    print()
