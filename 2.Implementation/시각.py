def solution(N):
    # 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각중 3이 하나라도 포함되는 모든 경우의  수 
    count = 0 
    # answer = [3, 13, 23, 30, 31, 32, 33, 34, 35 , 36, 37, 38, 39, 43, 53]
    for hours in range(N+1):
        for mins in range(0,60):
            for secs in range(0,60):
                if "3" in str(hours)+str(mins)+str(secs):
                    print(str(hours)+str(mins)+str(secs))
                    count+=1
        # 시도는 좋았으나.. 정답이 아님. 왜 정답이 아닌건지?고민해보기 
        #         if "3" in str(secs):
        #             count +=1 
        #             print("secs >> ",count)
        #     if "3" in str(mins):               
        #         count+=1
        #         print("mins >> ",count)
        # if "3" in str(hours):
        #     count+=1
        #     print("hours >> ",count)
    return count




if __name__ =="__main__":
    # n= 5 --> 11475
    N = int(input())
    print(solution(N))