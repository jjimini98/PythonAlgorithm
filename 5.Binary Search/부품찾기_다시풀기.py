import sys


def binary_search(start, find , list_name): # 시작인덱스, 마지막 인덱스, 찾으려는 값 / binary search 는 yes, no를 return  
    start = start
    end = len(list_name) -1
    
    while start <= end:  # while 조건식이 계속해서 참일 때 while문이 돌아감. 
        mid = (start+end)//2  # 계속 값이 갱신되어야하므로 while문 안에 들어가는게 맞음 
        if list_name[mid] == find:
            return "yes"
        elif list_name[mid] > find:
            end = mid-1
        else: 
            start = mid+1 
    return "no"
    #     if list_name[mid] > find : 
    #        end = mid-1
    #     elif list_name[mid] < find : 
    #         start = mid+1
    #     elif list_name[mid] == find: 
    #         return "yes"
    #     else: return "no" 
    # return "no"

def solution(N_list, M_list):
    N_list.sort()
    for element in M_list:
        answer = binary_search(0, element,N_list) 
        print(answer, end= " ")



if __name__ == "__main__":
    N = int(sys.stdin.readline()) # 공장 안에 있는 부품 
    N_list = list(map(int, sys.stdin.readline().split()))
    
    M = int(sys.stdin.readline()) # 고객이 원하는 부품
    M_list = list(map(int, sys.stdin.readline().split()))

    solution(N_list, M_list) # solution은 결과를 print 해준다. return nono 
