

def sum_number(*arg):
    number_sum = sum(arg)
    return number_sum


def subtraction_number(*arg):
    number_subtraction = arg[0]
    for i in arg[1:]:
        number_subtraction -= i
    return number_subtraction


def  multiplication_number(*arg):
    number_multiplication = 1
    for i in arg:
        number_multiplication *= i
    return number_multiplication


def division_number(*arg):
    number_division = arg[0] / arg[1]
    return number_division


    
def calculater():
    dic_fuc = {
        "1" : (sum_number, "Please select the number you want to add, you can use a space to separate: "), 
        "2" : (subtraction_number, "Please select the numbers you want to subtract. You can use Spaces to separate them: "),
        "3" : (multiplication_number, "Please select the numbers you want to multiply, separated by Spaces: "),
        "4" : (division_number, "division number(choice two)(Separate them with Spaces): "),
        }
    while True:
        ask = input("1. add\n2. subtraction\n3. multiplication_number\n4. division_number\nq. exit\nchoice one: ")

        if ask.upper() == "Q":
            break

        fun_tuple = dic_fuc.get(ask)

        if fun_tuple is None:
            print("no this choice")
            continue

        number_ask = input(fun_tuple[1]).strip().split(" ")
        number_list = []

        for i in number_ask:
            try:
                number_list.append(int(i))
            except:
                pass

        # if ask in ["1","2","3"] and len(number_list) != 3:
        #     print("choice three number!")
        #     continue

        if ask == "4" and len(number_list) != 2:
            print("choice two number!")
            continue

        print(f"\nYou've got: {fun_tuple[0](*number_list)}\n")


def run():
    if __name__ == "__main__":
        calculater()
        

run()
















