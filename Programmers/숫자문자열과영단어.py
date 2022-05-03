# find 하고 있으면 새로운 문자열에 넣기 


numbers = ["zero" ,"one","two" ,"three","four","five" , "six", "seven" ,"eight","nine"]

def solution(s):
    
    for num in numbers:
        if s.find(num) != -1:
            s = s.replace(num, str(numbers.index(num)))
    return int(s)


if __name__ == "__main__":
    s = "23fourfour5six7"
    print(solution(s))