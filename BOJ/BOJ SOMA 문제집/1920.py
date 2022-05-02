import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))

M = int(input())
M_list = list(map(int,input().split()))

def search(target):
    N_list.sort()
    start = 0
    end = len(N_list) - 1

    while start <= end: 
        mid = (start+end)//2

        if N_list[mid] == target:
            return 1 
        elif N_list[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1 
    return 0 

for m in M_list:
    print(search(m))
    
# 시간 초과
#     if m in N_list:
#         print(1)
#     else: 
#         print(0)
