def solution(price,money,count):
    total = 0 
    for x in range(1,count+1):
        total += (price*x)
    
    if total-money <=0 :
        return 0 
    return total-money 




if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    answer = solution(price, money, count)
    print(answer)