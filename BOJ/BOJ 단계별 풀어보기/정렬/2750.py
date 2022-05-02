

numbers = [int(input()) for _ in range(int(input()))] # 시간 복잡도 : O(N)

for x in sorted(numbers): # 시간 복잡도 : O(NlogN)
    print(x)

# 전체 시간 복잡도 : O(NlogN)