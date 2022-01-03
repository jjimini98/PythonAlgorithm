graph = [[] for _ in range(3)] #행의 길이가 3인 2차원 리스트 

graph[0].append((1,7)) #0과 연결된 노드와 거리 
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)