N,M,K = list(map(int,input().split()))
number = list(map(int, input().split()))

number = sorted(number,reverse=True)

one,two = number[0],number[1]

sum = 0 
while True:
    for _ in range(K):
        sum += one
        M -= 1 
        if M == 0 : break
    sum += two
    M -= 1 
    if M==0: break
print(sum)