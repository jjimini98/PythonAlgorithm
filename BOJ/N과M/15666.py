from itertools import combinations_with_replacement

N, M = map(int, input().split())
N_list = sorted(set(map(int,input().split())))

for pro in combinations_with_replacement(N_list, M):
    print(*pro)

