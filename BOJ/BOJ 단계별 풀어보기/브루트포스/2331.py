# 2331. 분해합
import sys

N = int(sys.stdin.readline())

for num in range(N, 0, -1): 
    total = num
    for x in range(len(str(num)), 0 , -1):
        ing = num % 10**(x-1) # 16
        val = ing // 10**(x-1) # 2 
        total += val   

        # if total == N : 
        #     print(num)