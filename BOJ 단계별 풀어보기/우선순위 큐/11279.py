import heapq 
import sys 

N = int(sys.stdin.readline())
result = [] 
answer = [] 

for _ in range(N) :
    input_number = int(sys.stdin.readline())
    if input_number == 0 :
        if len(result) == 0 : answer.append(0)
        else: answer.append(-heapq.heappop(result)) #최대 힙으로 출력하려면 앞에 -를 붙여서 다시 양수로 만들어줘야함 
    else:
        heapq.heappush(result,-input_number) #최대 힙을 구현하려면 앞에 - 를 붙여야함 

for x in answer:
    print(x)
    