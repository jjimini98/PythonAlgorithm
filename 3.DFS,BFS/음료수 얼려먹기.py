#얼음틀 사이즈 입력
N,M = map(int, input().split())
ice_tray = [list(map(int, input())) for _ in range(N)]
result = 0 

def solution(x,y):

    #x랑 y가 범위를 벗어나는 경우도 고려 
    if x <= -1 or  x >= N or y <= -1 or y >= M : 
        return False 

    #0 인걸 확인하면 0을 1로 바꾸고 return 해주기
    if ice_tray[x][y] == 0 : 
        ice_tray[x][y] = 1 
        solution(x-1,y)
        solution(x+1,y)
        solution(x,y+1)
        solution(x,y-1)
        return True
    
    return False


for i in range(N):
    for j in range(M):
        if solution(i,j) == True: 
            result += 1
        
print(result)









# if __name__ == "__main__":
#     graph = [
#         [0,0,1],
#         [0,1,0],
#         [1,0,1]
#     ]
    
    
#     # solution(graph)
#     print(len(graph))