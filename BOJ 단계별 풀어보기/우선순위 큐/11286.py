from heapq import * 
import sys

input = sys.stdin.readline

result = []
answer = [] #값 자체가 담겨야함 
temp = [] 

for _ in range(int(input())):
    input_number = int(input())
    if input_number == 0 :
        if len(result) == 0 : 
            answer.append(0)
        else: 
            prior_result = sorted(result, key= lambda x : abs(x))
            for x in prior_result:
                temp.append((prior_result.index(x)+1,x))
            answer.append(heappop(temp)) 
    else:
        heappush(result,input_number)
        
print("===============================================")
for x in answer:
    print(x)
    

