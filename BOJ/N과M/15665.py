from itertools import product

N, M = map(int, input().split())
N_list = sorted(set(map(int,input().split())))

for pro in product(N_list, repeat=M):
    print(*pro)

