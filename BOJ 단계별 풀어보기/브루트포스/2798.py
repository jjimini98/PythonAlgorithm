# 2798. 블랙잭
from ast import Num
import sys

N, M = map(int, sys.stdin.readline().split(" "))
Numbers = sorted(list(map(int, sys.stdin.readline().split())),reverse=True)

count = 3 
answer = 0 
x = 0 

for num in Numbers[x:]:
    print("현재 num >> ", num)
    M -= num
    answer += num
    count -= 1
    if M < Numbers[-1] and count !=0:
        x += 1
        print("this?")
print(answer)