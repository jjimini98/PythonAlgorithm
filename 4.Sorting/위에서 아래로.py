def solution(arr:list):
    arr = sorted(arr,reverse=True)
    for x in arr: print(x , end = " ")

if __name__ == "__main__":
    array = [int(input()) for _ in range(int(input())) ] 
    solution(array)