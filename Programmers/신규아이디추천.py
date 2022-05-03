import re 


def remove_unique(user_id):
    user_id = re.sub(r"[^a-zA-Z0-9_\.-]",'',user_id)
    user_id = re.sub(r"\.+",".",user_id)
    user_id = re.sub(r"^[.]|[.]$",'',user_id)
    return user_id

def re_length(user_id):

    if len(user_id) == 0:
        user_id = "a"

    elif len(user_id) >= 16:
        user_id = user_id[:15]
        user_id =  re.sub('^[.]|[.]$', '', user_id)


    if len(user_id) <= 2:
        for _ in range(3-len(user_id)):
            user_id += user_id[-1]

    return user_id 


def solution(user_id) : 
    user_id = user_id.lower()
    return  re_length(remove_unique(user_id))

if __name__ == "__main__":
    # user_id = ".......!@BaT#*..y.abcdefghijklm"
    # user_id ="-.~!@#$%&*()=+[{]}:?,<>/.-"
    user_id = "a...a"
    print(solution(user_id))