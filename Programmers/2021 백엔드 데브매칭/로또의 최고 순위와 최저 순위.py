def solution(lottos, win_nums):
    
    answer = []

    set_lottos = set(lottos)
    set_win_nums= set(win_nums)

    min_lotto = len(list(set_lottos&set_win_nums))
    max_lotto = min_lotto + find_zero(lottos)


    answer.append(rank(max_lotto))
    answer.append(rank(min_lotto))
    return answer

def find_zero(lotto:list):
    count = 0 

    for x in lotto:
        if x == 0:
            count+=1
    

    return count



def rank(lotto):
    if lotto == 6 : 
        return 1 
    elif lotto == 5 :
        return 2
    elif lotto == 4:
        return 3
    elif lotto == 3:
        return 4
    elif lotto == 2:
        return 5
    else: 
        return 6 

if __name__ == "__main__":
    lottos = [0, 4, 35, 20, 3, 9]
    win = [20, 9, 3, 45, 4, 35]

    print(solution(lottos,win))