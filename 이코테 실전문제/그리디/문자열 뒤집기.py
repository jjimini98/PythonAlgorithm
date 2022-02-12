# 1439. 뒤집기 (출처 : 백준)

S = input()


count = 0
number = int(S[0])
temp = list()

for s in S:
    if int(s) != number:
        temp.append(s)
        if s == S[-1]: 
            count +=1

    else: 
        if len(temp) > 0 :
            count +=1 
            del temp[:]


print(count)




## 카운터를 쓰는 방식!!! 맨처음에 내가 생각했던 아이디어를 구현할 수 있음 모르겠다 근데;;; 
# from collections import Counter

# # c = Counter()
# # c = Counter("11001100110011000001")
# c = "11001100110011000001"
# print(c.split("0"))
