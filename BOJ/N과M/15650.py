from itertools import combinations

N,M = map(int, input().split())

for com in combinations(range(1,N+1),M):
    print(*com)

