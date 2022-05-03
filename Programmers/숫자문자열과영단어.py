# find 하고 있으면 새로운 문자열에 넣기 



def solution(s):
    numbers = ["zero" ,"one","two" ,"three","four","five" , "six", "seven" ,"eight","nine"]
    for num in numbers:
        s = s.replace(num, str(numbers.index(num))) #replace가 다 변경해줌. find 이런거 필요없겠군.. 
    return int(s)


if __name__ == "__main__":
    s = "23fourfour5six7"
    print(solution(s))


# 다른사람 풀이
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)