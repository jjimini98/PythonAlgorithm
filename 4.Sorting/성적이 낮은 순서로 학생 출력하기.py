def solution(arr): 
    for i in sorted(arr, key=lambda x : int(x[1])) :
        print(i[0], end = ' ')


if __name__ == "__main__":
    arr = [tuple(input().split()) for _ in range(int(input()))]
    solution(arr)