def solution(limit,route):
    x, y = 1, 1
    for direction in route:
        if direction == "R" :
            y +=1 
            if x==0 or y==0 or x>limit or y>limit :
                y -= 1 
        elif direction == "L":
            y -=1
            if x==0 or y==0 or x>limit or y>limit :
                y += 1 
        elif direction == "U": 
            x -=1
            if x==0 or y==0 or x>limit or y>limit : 
                x +=1 
        elif direction == "D": 
            x +=1 
            if x==0 or y==0 or x>limit or y>limit :
                x -=1 
            
    
    print("final : " , x,y)
    return x,y 




if __name__ == "__main__":
    limit = int(input())
    route = input().split()
    solution(limit, route)