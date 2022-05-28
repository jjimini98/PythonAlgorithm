from itertools import product


N, M = map(int, input().split())
N_list = sorted(list(map(int,input().split())))

for pro in product(N_list, repeat=M):
    print(*pro)