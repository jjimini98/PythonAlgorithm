import sys

def myanswer() : 
    N, M = sys.stdin.readline().split()

    # 가장 작은 값들을 리스트에 저장한 후 값을 추출 하는 방법 
    min_result = list()

    for _ in range(int(N)):
        row = list(map(int, sys.stdin.readline().split()))
        min_result.append(min(row))

    print(max(min_result))


def bookanswer():
    N, M = sys.stdin.readline().split()

    max_value = 0 # 이렇게 하면 굳이 리스트를 만들지 않아도 된다 ! 
    for _ in range(int(N)):
        row = list(map(int, sys.stdin.readline().split()))
        min_value = min(row)
        max_value = max(max_value, min_value)
    print(max_value)

if __name__ == "__main__":
    # myanswer()
    bookanswer()
