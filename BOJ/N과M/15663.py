from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int,input().split()))

answer = sorted(set([com for com in permutations(N_list, M) ]))


for x in answer:
    print(*x)
