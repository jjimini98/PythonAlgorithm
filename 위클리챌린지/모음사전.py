# def solution(word):
#     alphabet = ['A','E',"I","O","U"]
#     dictionary = ['','','','','']
#     current_alphabet = ''
#     count = 1 

#     # iter_alphabet = alphabet.remove(moeum)
#     for moeum in alphabet:  
#         for idx in range(len(dictionary)):
#             dictionary[idx]=moeum
#             # print(dictionary)
#         iter_alphabet = alphabet.remove(moeum)
#         reverse_dictionary = list(reversed(dictionary))
#         for idx,re_moeum in enumerate(reverse_dictionary):
#             dictionary[idx]=re_moeum
#             print(list(reversed(dictionary)))


	
def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        print(w)
                        break
                        if w not in ans: ans.append(w)
    ans.sort()
    # print(ans)
    answer = ans.index(word)
    return answer




if __name__ == "__main__":
    word1 = "AAAAE" 
    word2 = "AAAE"
    word3 = "I"
    word4 = "EIO"
    lis = ['A','E',"I"]
    for x in lis:
        for y in lis:
            for z in lis:
                print(x+y+z)

    # solution(word1)
    # solution(word2)
    # solution(word3)
    # solution(word4)