def solution(a, b):
    answer = 0
    
    for x in range(len(a)):
        answer += a[x]*b[x]

    return answer



if __name__ == "__main__":
    a = [1,2,3,4]
    b = [-3,-1,0,2]
    print(solution(a,b))