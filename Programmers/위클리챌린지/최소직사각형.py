def solution(sizes):
    # answer = 0 
    # temp = list()
    # x,y = 0,0
    # for element in sizes:
    #     x = max(x,element[0])
    #     y = max(y,element[1])
    # critria = min(x,y)
    # x,y = 0,0
    # for element in sizes:
    #     if critria in element:
    #         sizes[element.index(critria)].reverse()
            
    #     x = max(x,element[0])
    #     y = max(y,element[1])
    # print(x,y)
    # return x*y
    # ==========================================================================
    # critria = min(x,y)
    # answer = 0 
    # arr = list()
    # for element in sizes:
    #     arr.extend(element)
    #     arr.sort()
    # median = len(arr)//2-1
    # one = max(arr[:median+1])
    # two = max(arr[median:])
    # answer = one*two 

    # return answer

    # print(max(max(x) for x in sizes))
    # print(max(min(x) for x in sizes))
    for x in sizes:
        print(x)
        print(max(x))

    return max(max(x) for x in sizes) * max(min(x) for x in sizes)





if __name__ == "__main__":
    sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
    sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    answer1 = solution(sizes1)
    answer2 = solution(sizes2)
    answer3 = solution(sizes3)
    # print(answer1)
    # print(answer2)
    # print(answer3)