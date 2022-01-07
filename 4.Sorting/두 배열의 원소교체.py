def solution(A,B,K):
    # sum = 0 
    A.sort()
    B.sort(reverse=True)
    # 이렇게 하면 A가 B보다 큰 경우에도 값을 바꿔버림.. B가 더 클 때만 바꾸도록 설정 
    # for x in range(K):
    #     A[x],B[x] = B[x],A[x]
    for x in range(K):
        if A[x] < B[x]: A[x],B[x] = B[x],A[x]
        else: continue
    
    # sum 함수를 쓰자 
    # for a in A:
    #     sum +=a 
    
    return sum(A)



if __name__ == "__main__":
    N,K = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    print(solution(A,B,K))
