
N = int(input())
storage = list(map(int, input().split())) # [1,3,1,5]

d = [0] * 101

d[0] = storage[0]  
d[1] = max(storage[0], storage[1])

for x in range(2,N):
    d[x] = max(d[x-1], d[x-2]+storage[x])

print(d[x])

