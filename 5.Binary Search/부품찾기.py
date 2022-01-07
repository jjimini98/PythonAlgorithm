import sys

def binary_search(arr:list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > target: 
            end = mid-1
        elif arr[mid] == target: return "yes"
        else: start = mid+1 
    return "no"
    # if start >= end: return "No"
    # mid = (start+end)//2
    # if arr[mid] < target: 
    #     binary_search(arr, target, start, mid-1)
    # elif arr[mid] == target : return "Yes"
    # else : binary_search(arr, target, mid+1, end)











def solution(N, N_list, M, M_list):
    N_list = sorted(N_list)
    for x in M_list:
        result = binary_search(N_list,x,0,N-1)
        print(result, end=' ')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    N_list = list(map(int, sys.stdin.readline().split(" ")))
    M = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split()))

    solution(N,N_list,M,M_list)