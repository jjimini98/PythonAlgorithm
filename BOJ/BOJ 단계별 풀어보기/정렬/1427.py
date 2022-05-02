# 1427. 소트인사이드

number = int(input())
number = sorted(str(number), reverse=True)
print(int(''.join(number)))
