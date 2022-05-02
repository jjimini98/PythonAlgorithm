#9095 1,2,3 더하기  -> 다시! 

import sys

input = sys.stdin.readline

d = [x for x in range(100)]
def recursive(x):
    if x == 0: 
        return 0
    elif x == 1: 
        return 1 
    elif x == 2 : 
        return 2
    elif x == 3 : 
        return 4 
    else: 
        return recursive(x-3) + recursive(x-2) + recursive(x-1)

for _ in range(int(input())):
    num = int(input())
    d[num] = recursive(num) 
    print(d[num])

