from itertools import combinations_with_replacement


N, M = map(int, input().split())
N_list = sorted(list(map(int,input().split())))

for com in combinations_with_replacement(N_list, M):
    print(*com)