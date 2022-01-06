from collections import deque

#  미로 사이즈 입력받기
N, M = map(int, input().split())
miro = [list(map(int,input())) for _ in range(N)]
start = [1,1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue : 
        x,y = queue.popleft()
        # 아래 더 추가해야함 