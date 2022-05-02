# 7568. 덩치
import sys

people = list()
rank = str()
for _ in range(int(sys.stdin.readline())):
    people.append(tuple(map(int, sys.stdin.readline().split())))



for one in people:
    count = 0 
    for two in people: 
        if one[0] < two[0] and one[1] < two[1]:
            count +=1 

    rank += str(count+1) + " "

print(rank)