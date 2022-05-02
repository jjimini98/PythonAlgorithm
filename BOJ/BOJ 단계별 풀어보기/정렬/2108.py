# 2108. 통계학
from collections import Counter
import sys 
# 일단 전체 필요한 수 입력받기
numbers = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]


# 1. 산술평균
print(round(sum(numbers) / len(numbers)))

# 2. 중앙값
print(sorted(numbers)[len(numbers)//2]) #복잡도 : NlogN

# 3. 최빈값
cnt = Counter(numbers).most_common()

big = cnt[0][1]
lis = []

for x in cnt: # 복잡도를 줄인게 신의 한수! 
    if x[1] == big:
        lis.append(x)
    
if len(lis) != 1:
    lis = sorted(lis)
    print(lis[1][0])
else: 
    print(lis[0][0])



# 4. 범위
min_value = min(numbers)
max_value = max(numbers)


if max_value > 0 and min_value > 0 :
    print(max_value-min_value)
elif max_value > 0 and min_value < 0 :
    print(max_value - min_value)
else:
    print(abs(abs(max_value) - abs(min_value)))