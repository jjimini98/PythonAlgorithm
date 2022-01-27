from itsdangerous import exc
from sklearn.metrics import multilabel_confusion_matrix


def solution(len_list,lis):
    max_value = 0 
    for i in range(len_list):
        try: 
            for j in range(i+2, len_list):  
                max_value = max(max_value , lis[i] + lis[j]) 
        except: 
            continue
    
    return max_value





if __name__ == "__main__":
    len_list = int(input())
    lis = list(map(int, input().split() ))
    value = solution(len_list,lis)
    print(value)