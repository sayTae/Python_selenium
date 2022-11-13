
def Userdata():
    file = open("sskk/User_data.txt", "r", encoding="UTF-8")
    User_id, User_pw, HowManyListen = list(map(str, file.read().split()))
    file.close()
    
    return User_id, User_pw, HowManyListen