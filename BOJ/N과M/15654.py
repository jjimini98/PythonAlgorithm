from itertools import permutations


N, M = map(int, input().split())
N_list = sorted(list(map(int,input().split())))

for per in permutations(N_list, M):
    print(*per)