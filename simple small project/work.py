# class Project:
#     def __init__(self,) -> None:
#         self.infomation = {"project" : str, "total_budget" : float, "current_budget_get" : float, 
#                            "employees" : {"name": list, "salary": float, "position": str},}

import csv 
import pandas as pd

def chick_file_is_exist(path):
    try:
        with open(path,mode="r") as file:
            file.close()
    except:
        build_csv(path) 

def chick_is_num(text):
        while True:
            try:
                num = input(text)
                int(num)
                return num
            except:
                print("wrong values")
                continue

def ask_project_infomation():
    project_name = input("what is project name: ")
    total_budget = chick_is_num("how much about total budget: ")
    current_budget_get = chick_is_num("how much current budget get: ")
    employees_name_list = input("who is employees(If you have a majority of employees, you can use commas to divide them): ").strip(",").split(",")
    employees_salary = chick_is_num("how much about employees salary: ")
    employees_position = input("what is employees position: ")
    
    return {"project" : project_name, "total_budget" : total_budget, "current_budget_get" : current_budget_get, 
            "employees_name_list": employees_name_list, "employees_salary": employees_salary, "employees_position": employees_position}

def del_project(project_name,path_list):
    data = pd.read_csv(path_list[0])
    data[data["project"] != project_name].to_csv(path_list[0],index=False,sep=',')
    data[data["project"] == project_name].to_csv(path_list[1],index=False,header=False,sep=',',mode="a")

def build_csv(path):
    fields = ['project', 'total_budget', 'current_budget_get', 'employees_name_list', 'employees_salary', 'employees_position']
    with open(path, mode='w', newline="") as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        writer.writeheader()




def add_project(PATH_1):
    with open(PATH_1,mode="a",newline="") as file:
        write = csv.DictWriter(file,fieldnames=['project', 'total_budget', 'current_budget_get', 'employees_name_list', 'employees_salary', 'employees_position'])
        write.writerow(ask_project_infomation())
        
def chick_project(path_list):
    ask = input("1, view all projects(input 1)\n2, view executable project(input 2)\n3, view deleted items(input 3)\n(The default option is Deleted project):")
    data_1 = pd.read_csv(path_list[0])
    data_2 = pd.read_csv(path_list[1])
    if ask == "1":
        data_3 = pd.concat([data_1,data_2],axis=0,ignore_index=True)
        print(data_3)
    elif ask == "2":
        print(data_1)
    else:
        print(data_2)

def change_project_infomation(path_list):
    project_name = input("Please enter the name of the project you want to change to get the budget: ")
    data = pd.read_csv(path_list[0])
    print("Here is the project information:")
    print(data[data["project"]==project_name])
    if data[data["project"]==project_name].empty:
        return
    current_budget_get = chick_is_num("The current budget obtained is: ")
    data.loc[data["project"]==project_name,"current_budget_get"]=current_budget_get
    if (int(data.loc[data["project"]==project_name,"current_budget_get"]) + int(data.loc[data["project"]==project_name,"employees_salary"]) == int(data.loc[data["project"]==project_name,"total_budget"])):
        del_project(project_name,path_list)
    else:
        data.to_csv(path_list[0],index=False,sep=',')



def main():
    
    PATH_1 = "projects.csv"
    PATH_2 = "projects_del.csv"
    FUNCTION_DIC = {
        "1": [add_project,PATH_1],
        "2": [chick_project,[PATH_1,PATH_2]],
        "3": [change_project_infomation,[PATH_1,PATH_2]],
        "4": "quit"      
    }

    chick_file_is_exist(PATH_1)
    chick_file_is_exist(PATH_2)
    
    while True:
        ask = input("Choose the service you need:\n1, add project(input 1)\n2, chick project(input 2)\n3, change project infomation(input 3)\n4, quit(input 4)\n: ")
        fun_list = FUNCTION_DIC.get(ask)
        if fun_list == None:
            print("invalid input")
            continue
        if fun_list == "quit":
            break
        fun = fun_list[0]
        fun(fun_list[1])

if __name__ == "__main__":
    main()










