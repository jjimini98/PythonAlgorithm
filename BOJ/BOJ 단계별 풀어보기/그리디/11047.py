# 11047. 동전 0 
from sys import stdin

N, K = map(int, stdin.readline().split())
coin_list = sorted([int(stdin.readline()) for _ in range(N)],reverse=True)
count = 0 

for coin in coin_list:
    if K >= coin : 
        count += K//coin
        K = K%coin
print(count)

# for coin in coin_list: 
# while K >= coin : 
#     K = K-coin 
#     count +=1 
#     if K == 0 : break 