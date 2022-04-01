# 12852. 1로 만들기 2 

import sys

X = int(sys.stdin.readline())

answer = 0 
proceed = []

while X != 0:
    if X%3 == 0 : 
        proceed.append(X)
        X = X//3
        # answer += 1

    elif X%2 == 0:
        proceed.append(X)
        X = X//2
        # answer += 1 
    else:
        proceed.append(X)
        X -= 1 
        # answer += 1

print(len(proceed)-1)
for x in proceed:
    print(x, end=' ')