
from collections import deque

N,M = map(int,input().split())
graph = [list(map(int, input())) for _ in range(N)] 

start = 0 


def bfs(x,y): 

    answer = 0 
    queue = deque([])
    if x== 0 and y == 0 : 
        queue.append((x,y))
        answer += 1


    while queue:
        if x >= N or x < 0 or y >= M or y< 0: 
            return False 

        queue.popleft()

        if graph[x+1][y] == 1: 
            queue.append((x+1,y)) 
            graph[x+1][y] = 0
            answer += 1
        if graph[x-1][y] == 1:
            queue.append((x-1,y))
            graph[x-1][y] = 0
            answer += 1
        if graph[x][y+1]  == 1:
            queue.append((x,y+1))
            graph[x][y+1] = 0
            answer += 1
        if graph[x][y-1] == 1:
            queue.append((x,y-1))
            graph[x][y-1] = 0 
            answer += 1

    return answer 


for x in range(N):
    for y in range(M): 
        print(bfs(x,y)) 
