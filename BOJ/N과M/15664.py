from itertools import combinations

N, M = map(int, input().split())
N_list = sorted(list(map(int,input().split())))
answer = [] 



for com in combinations(N_list,M):
    if com in answer:
        continue
    else:
        answer.append(com)

for x in sorted(answer):
    print(*x)
