# 프로그래머스

def solution(n, lost, reserve):
    answer = n - len(lost)
 
    for x in reserve:
        for y in lost : 
            if abs(x-y) == 1 :
                reserve.pop(reserve.index(x))
                lost.pop(lost.index(y))
                answer +=1
    return answer




if __name__ == "__main__":
    N = 10
    # lost = [2,4]
    lost = [3,6,9]
    # reserve = [1,3,5]
    reserve = [1,2,5,6]
    result = solution(N, lost, reserve)
    print(result)