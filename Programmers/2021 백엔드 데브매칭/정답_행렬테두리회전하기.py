def solution(rows, columns, queries):
    answer = []
    tables = []

    for r in range(rows):
        tables.append([a for a in range(r*columns+1 , (r+1)*columns+1)])

    for query in queries:
        query = [x-1 for x in query]
        tmp = tables[query[0]][query[1]]
        small = tmp

        for i in range(query[0]+1 , query[2]+1):
            tables[i-1][query[1]] = tables[i][query[1]]
            small = min(small, tables[i][query[1]])

        for i in range(query[1]+1 , query[3]+1):
            tables[query[2]][i-1] = tables[query[2]][i]
            small = min(small, tables[query[2]][i])

        for i in range(query[2]-1 , query[0]-1 , -1) :
            tables[i+1][query[3]]  = tables[i][query[3]]
            small = min(small, tables[query[3]][i])

        for i in range(query[3]-1, query[1]-1, -1):
            tables[query[0]][i+1] = tables[query[0]][i]
            small = min(small , tables[query[0]][i])
        tables[query[0]]





if __name__ == "__main__":
    rows = 6
    columns = 6
    queries = [[2,2,5,4]]
    solution(rows,columns,queries)