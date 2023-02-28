
def ask_login(dict):
    while True:
        user_account = input("Enter your account(q is quit): ")
        if user_account.upper() == "Q":
            break
        if user_account not in dict.keys():
            print("unfound")
            continue
        for i in range(3): 
            password = input("Enter your password: ")
            if dict[user_account][0] == password:
                i=0
                break
            print("wrong password !, you have {}/3 times".format(i+1))
        if i == 2:
            break
        print("Login successfully")
        print(id(dict))
        break
    return user_account
        

def ask_register(dict):
    user_account = input("Enter your account: ")
    password = input("Enter your password: ")
    dict[user_account] = [password,0,"OCTC"]
    print(id(dict))
    print("Registration successful")


def query_account_information(dict):
    while True:
        user_account = input("Enter your account(q is quit): ")
        if user_account.upper() == "Q":
            break
        if user_account not in dict.keys():
            print("unfound")
            continue
        print("blance: {}".format(dict[user_account][1]))
        print("bank_code: {}\n".format(dict[user_account][2]))
        print(id(dict))
        


def save_money(user_account,dict):
    money = input("how much you want to save: ")
    dict[user_account][1] += int(money)
    print(id(dict),id(user_account))


def draw_money(user_account,dict):
    money = input("how much you want to draw: ")
    if dict[user_account][1] >= int(money):
        dict[user_account][1] -= int(money)
    else:
        print("no much money\n")
    print(id(dict),id(user_account))


def run():
    dict_bank = {}
    fun_dict={
        "1": ask_login,
        "2": ask_register,
        "3": query_account_information,
    }
    fun_dict_2 = {
        "1": save_money,
        "2": draw_money,
    }
    while True:
        ask = input("1, login\n2, register\n3, query\n4, quit\n: ")
        if ask == "4":
            break

        fun = fun_dict.get(ask)
        if fun is None:
            print("error")
            continue

        user_account = fun(dict_bank) 
        if user_account is None or user_account.upper() == "Q":
            continue

        while True:
            ask_save_or_draw = input("1, save money\n2, draw money\n3, quit\n: ")
            if ask_save_or_draw == "3":
                break

            fun = fun_dict_2.get(ask_save_or_draw)
            if fun is None:
                break

            fun(user_account,dict_bank)


run()
"""
id(dict) -> dict_bank
id(user_account) -> ask_login(dict)
"""


