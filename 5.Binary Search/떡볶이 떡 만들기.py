#이진탐색 없이 내가 짠 코드

import sys

def solution(M, dduk): # M이 원하는 떡 개수임 
    
    dduk.sort()
    for x in range(dduk[0], dduk[-1]): #x 절단기 길이 
        sum = 0
        for dduk_hana in dduk: # 주어진 떡의 길이 
            if x < dduk_hana: # 절단기 길이가 떡길이보다 작아야 잘린다. 
                sum += abs(dduk_hana-x)
        if sum == M : 
            print(x)

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    dduk = list(map(int, sys.stdin.readline().split()))
    solution(M,dduk)
    # answer = solution(M, dduk)
    # print(answer)