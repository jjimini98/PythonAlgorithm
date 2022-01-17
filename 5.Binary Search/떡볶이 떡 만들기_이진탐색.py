import sys 

def solution(target, arr): 
    start = 0 
    end = max(arr) 

    result = 0 

    while start<=end:
        total = 0 
        mid = (start+end)//2
        for x in arr: 
            if x > mid: # 절단기 위치보다 작은 떡은 고려하지 않음 
                total += x-mid #잘린 총 떡이 total 
        
        if total < target :
            end = mid -1 # 절단기의 위치를 더 앞으로 땡겨서 많은 떡이 잘리게 한다. 
        else: 
            result = mid #total이 더크면 result에 mid 값을 넣고 
            start = mid +1 # 절단기의 위치를 더뒤로 밀어서 더 적은 떡이 잘리게 한다. 
        

    return result 





if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    answer = solution(M,array)   
    print(answer)