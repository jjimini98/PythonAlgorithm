import sys

input = sys.stdin.readline


for _ in range(int(input())):
    result = input()
    stack = []
    score = 0 
    for x in result:
        if x == "O":
            stack.append("O")
        else:
            for t in range(1,len(stack)+1):
                score += t
            stack = []

    print(score)