from itertools import combinations


N, M = map(int, input().split())
N_list = sorted(list(map(int,input().split())))

for com in combinations(N_list, M):
    print(*com)