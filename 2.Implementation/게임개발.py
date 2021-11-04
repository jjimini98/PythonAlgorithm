# def turn_left(current_x, current_y , direction):
#     if direction == 0 :
#         current_x -=1 
#         direction = 3
#     elif direction == 1 :
#         current_y -=1
#         direction = 0
#     elif direction == 2 : 
#         current_x +=1 
#         direction = 1 
#     elif direction == 3:
#         current_y +=1 
#         direction = 2

#     return direction, current_x , current_y
        


def solution(mapsize_x,mapsize_y,default_x,default_y,direction,total_map):
    current = total_map[default_x][default_y]
    count = 0 
    while True:  # while True 로 하고 값을 계속 업데이트하는게 나을 것 같음 그리고 종료조건 명시 
        if direction == 0 :     
            default_x -=1 
            direction = 3
            current = total_map[default_x][default_y]
            # if current == 0 : break 
        elif direction == 1 :
            default_y -=1
            direction = 0
            current = total_map[default_x][default_y]
            if current == 0 : 
                default_x +=1 
                current = total_map[default_x][default_y]
                # break 
        elif direction == 2 : 
            default_x +=1 
            direction = 1 
            current = total_map[default_x][default_y]
            if current == 0 :
                default_x +=1 
                current = total_map[default_x][default_y]
                # break 
        elif direction == 3:
            default_y +=1 
            direction = 2
            current = total_map[default_x][default_y]
            # if current == 0 : break 

    print(direction)
    print(default_x,default_y)






if __name__ == "__main__":
    mapsize_x , mapsize_y = map(int, input().split())
    default_x,default_y,direction = map(int, input().split())
    total_map = list()
    for _ in range(mapsize_x):
        total_map.append(list(map(int, input().split())))
    answer = solution(mapsize_x,mapsize_y,default_x,default_y,direction,total_map)
    # print(answer)
    # print(mapsize_x,mapsize_y)
    # print(default_x, default_y, direction)
    # print(total_map)

# test case 
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

