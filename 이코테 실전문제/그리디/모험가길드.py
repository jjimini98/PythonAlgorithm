from socket import NI_NUMERICSERV
import sys

def solution(people : list):

    people.sort(reverse=True) #내림차순으로 정렬 

    number = people[0] #가장 첫번째 있는 값으로 초기화 
    count = 0 
    sum = 0 

    for person in people:  
        count+=1
        if count == number:
            sum+=1 
            number = people[people.index(person)+1]
            count = 0 
    
    return sum


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    people = list(map(int, sys.stdin.readline().split()))

    answer = solution(people)
    print(answer)