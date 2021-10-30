# 시간초과 
from itertools import combinations

def solution(number, k):
    length = len(number) - k 
    combi = list(combinations(number, length))
    result = 0
    for x in combi: 
        result = max(result , int(''.join(list(x))))
        

    return str(result)



# def solution(number, k):
#     center = len(number)//2
#     front = number[:center] 
#     back = number[center+1:]
#     target = 0
#     next_v = 1 
#     count = 0 
#     for x in range(center+1):
#         if front[x] > front[x+1]



if __name__ == "__main__":
    number = "4177252841"
    # number = "12345"
    k = 4
    # solution(number, k)
    max_value = solution(number, k)

    print(max_value)
