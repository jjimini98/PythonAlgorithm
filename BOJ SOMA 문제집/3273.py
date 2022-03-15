# 3273. 두 수의 합 : 투포인터 

# import sys, time 
# start = time.time()
# input = sys.stdin.readline

# n = int(input())
# sequence = sorted(list(map(int, input().split())))
# x = int(input())

# answer = 0 

# for s in sequence:
#     if x-s in sequence:
#         # sequence.remove(s)
#         answer += 1

# print(answer//2)
# print(time.time()- start)


# 다른 문제 풀이 방법 
# import sys, time 
# start_time = time.time()
# input = sys.stdin.readline

# n = int(input())
# sequence = sorted(list(map(int, input().split())))
# x = int(input())

# # start와 end 값을 계속 늘려가면서 값이 x랑 같아지면  count  
# # 값이 작으면, start 를 증가 , 값을 크면 end를 감소 
# start = 0
# end = n-1

# answer = 0 

# while start < n and end < n: 
#     if sequence[start] + sequence[end] == x : 
#         answer += 1
#         start += 1 
#         end -= 1
#         print("answer is ", answer)
#     elif sequence[start] + sequence[end] < x:
#         start +=1 
#         # print("start is ", start)
#     elif sequence[start] + sequence[end] > x:
#         end -= 1 
#         # print("end is ", end)
    
# print(answer//2)
     
# # print(answer//2)
# print(time.time()- start_time)



# 최종 코드 
import sys
input = sys.stdin.readline

n = int(input())
sequence = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, len(sequence) - 1

answer = 0 

while start < end:
    if sequence[start] + sequence[end] > x:
        end -= 1
    elif sequence[start] + sequence[end] < x:
        start += 1
    elif sequence[start] + sequence[end] == x :
            answer += 1 
            end -= 1
            start += 1

print(answer)