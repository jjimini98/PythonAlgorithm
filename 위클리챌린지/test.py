# 프로그래머스 테스트 문제

def solution(v):
    answer= list()
    x = sorted(list(map(lambda x:x[0], v))) # [1, 3, 3]
    y = sorted(list(map(lambda y:y[1], v))) # [4, 4, 10]
    answer.append(x[0]^x[1]^x[2])
    answer.append(y[0]^y[1]^y[2])
    return answer 


    # 내 코드 
    # x = []
    # y = [] 
    # for element in v : 
    #     if element[0] in x : 
    #         x.remove(element[0])
    #     else: 
    #         x.append(element[0])

    #     if element[1] in y:
    #         y.remove(element[1])
    #     else: 
    #         y.append(element[1]) 
    # answer = x+y
    # return answer 



if __name__ == "__main__":
    inputlist = [[1, 4], [3, 4], [3, 10]]
    # inputlist = [[1, 1], [2, 2], [1, 2]]
    answer = solution(inputlist)
    print(answer)
