def solution(rows, columns, queries):
    answer = []

    # 이중리스트 생성 
    tables =  []
    x = 1
    for _ in range(columns):
        table = [] 
        for _ in range(rows):
            table.append(x)
            x+=1 
        tables.append(table)

    # 테두리값 찾기 
    for query in queries:
        start = (query[0],query[1])
        end = (query[2],query[3])
        edges = dict() #테두리 값 담는 리스트 edge
        
        for x in range(start[0], end[0]+1):
            for y in range(start[1],end[1]+1):
                if x != start[0] and x != end[0] :
                    # edges.append((x,start[1]))
                    # edges.append((x,end[1]))
                    edges[(x,start[1])] = tables[x-1][start[1]-1]
                    edges[(x,end[1])] = tables[x-1][end[1]-1]
                else:
                    # edges.append((x,y))
                    edges[(x,y)] = tables[x-1][y-1]

        print(edges)

    # 시계방향으로 값 이동하기 
    for key,value in edges.items():
        key[0]
    # return answer






    

if __name__ == "__main__":
    rows = 6
    columns = 6 
    # queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    queries = [[2,2,5,4]]

    print(solution(rows, columns, queries))