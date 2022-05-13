import sys
while True:
    try:
        n = int(sys.stdin.readline())
        one = "1"
        while True: 
            if  int(one) % n == 0:
                print(len(str(one)))
                break 
            else:
                one = str(one) + "1"
    except:
        break

