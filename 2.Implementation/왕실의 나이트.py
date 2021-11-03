def solution(current_location):
    convert = ["a","b","c","d","e","f","g","h"]
    x,y = convert.index(current_location[0])+1 , int(current_location[1])
    count = 0 

    X = [2,2,-2,-2,-1,1,-1,1]
    Y = [1,-1,1,1,2,2,-2,-2]

    for i in range(len(X)):
        nx = x + X[i]
        ny = y + Y[i]

        if nx < 1 or ny < 1 or nx > 8 or ny > 8 : 
            continue
        count+=1

    return count 



if __name__ == "__main__":
    current = "a1"
    answer = solution(current)
    print(answer)