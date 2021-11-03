# def solution(limit,route):
#     x, y = 1, 1
#     for direction in route:
#         if direction == "R" :
#             y +=1 
#             if x==0 or y==0 or x>limit or y>limit :
#                 y -= 1 
#         elif direction == "L":
#             y -=1
#             if x==0 or y==0 or x>limit or y>limit :
#                 y += 1 
#         elif direction == "U": 
#             x -=1
#             if x==0 or y==0 or x>limit or y>limit : 
#                 x +=1 
#         elif direction == "D": 
#             x +=1 
#             if x==0 or y==0 or x>limit or y>limit :
#                 x -=1 
            
    
#     print("final : " , x,y)
#     return x,y 



def book_solution(limit,routes):
    x,y = 1,1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    direction = ["L","R","U","D"]
    
    for route in routes:
        for i in range(len(direction)):
            if route == direction[i]:
                nx = x + dx[i]
                ny = y + dy[i]
            
        if nx < 1 or ny < 1 or nx > limit or ny > limit:
            continue

        x,y = nx , ny 
    
    return x,y 





if __name__ == "__main__":
    limit = int(input())
    routes = input().split()
    print(book_solution(limit, routes))