#2579 계단 오르기
import sys

N = int(sys.stdin.readline())
d = [0 for _ in range(N+2)]
stairs = list()

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

d[1] = stairs[0]
d[2] = stairs[1]

for x in range(3,N+1): 
    d[x] = max(d[x-1]+stairs[x-1] , d[x-2]+stairs[x-1])

print(d) # 생각 자체는 좋았지만 부족한 점이 많음 

# 맨 마지막을 포함해야한다 -> 맨 마지막부터 시작  https://sungmin-joo.tistory.com/18
