from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue: #queue가 빈 리스트가 될 때까지 
        v = queue.popleft()
        print(v, end= " ")

        for i in graph[v]:
            if not visited[i]: # visited[i]가 False 일때 
                queue.append(i) 
                visited[i] = True



if __name__ == "__main__":
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited = [False for _ in range(len(graph))]
    
    bfs(graph,1,visited)