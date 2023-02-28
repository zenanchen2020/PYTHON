"""Write a program, that makes urdf link, calculates inertias of object, and saved it to xml file."""

"""m for mass, r for radius, w for width, h for height, d for depth"""
class Test:
    def text():
        global text_1
        text_1="\n"
    def ask_link_name():
        global link_name
        while True:
            link_name = input("what will be the link name, link name should start with link_ : ")
       
            if link_name.startswith("link_"):
                break
            else:
                print("Not a valid answer, try again.")
    def ask_shape():
        global shape
        while True:
            shape = input("What shape you want to use:"
                        "\n                      1 = Solid sphere"
                        "\n                      2 = Solid cuboid"
                        "\n                      3 = Solid cylinder ")
            if shape in ["1","2","3"]:
                break
            else:
                print("Not a valid answer, try again.")
    def shape_1():
        global text_1
        print("you choosed Solid sphere, give: mass, radius")
        while True:
            try:
                m = float(input("now give, mass as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                r = float(input("now give, radius as decimal number: "))
                break
            except:
                print("Not a vald answer, try again.")
        text_1 += (f'    <link name="{link_name}">'
               '\n      <inertial>'
              f'\n        <mass value="{m}"/>'
              f'\n        <inertia ixx="{2/5*(m*r**2)}" ixy="0.0" ixz="0.0" iyy="{2/5*(m*r**2)}" iyz="0.0" izz="{2/5*(m*r**2)}"/>'
               '\n      </inertial>'
               '\n      <visual>'
               '\n        <geometry>'
              f'\n          <sphere radius="{r}"/>'
               '\n        </geometry>'
               '\n      </visual>'
               '\n      <collision>'
               '\n        <geometry>'
              f'\n          <sphere radius="{r}"/>'
               '\n        </geometry>'
               '\n      </collision>'
               '\n    </link>\n')
    def shape_2():
        global text_1
        print("you choosed Solid cuboid, give: mass, width, height, depth")
        while True:
            try:
                m = float(input("now give, mass as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                w = float(input("now give, width as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                h = float(input("now give, height as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                d = float(input("now give, depth as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        text_1 += (f'    <link name="{link_name}">'
               '\n      <inertial>'
              f'\n        <mass value="{m}"/>'
              f'\n        <inertia ixx="{1/12*m*(h**2+d**2)}" ixy="0.0" ixz="0.0" iyy="{1/12*m*(w**2+h**2)}" iyz="0.0" izz="{1/12*m*(w**2+d**2)}"/>'
               '\n      </inertial>'
               '\n      <visual>'
               '\n        <geometry>'
              f'\n          <box size="{d} {w} {h}"/>'
               '\n        </geometry>'
               '\n      </visual>'
               '\n      <collision>'
               '\n        <geometry>'
              f'\n          <box size="{d} {w} {h}"/>'
               '\n        </geometry>'
               '\n      </collision>'
               '\n    </link>\n')
    def shape_3():
        global text_1
        print("you choosed Solid cylinder, give: mass, radius, height")
        while True:
            try:
                m = float(input("now give, mass as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                r = float(input("now give, radius as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        while True:
            try:
                h = float(input("now give, height as decimal number: "))
                break
            except:
                print("Not a valid answer, try again.")
        text_1 += (f'    <link name="{link_name}">'
               '\n      <inertial>'
              f'\n        <mass value="{m}"/>'
              f'\n        <inertia ixx="{1/12*m*(3*r**2+h**2)}" ixy="0.0" ixz="0.0" iyy="{1/12*m*(3*r**2+h**2)}" iyz="0.0" izz="{1/2*m*r**2}"/>'
               '\n      </inertial>'
               '\n      <visual>'
               '\n        <geometry>'
              f'\n          <cylinder length="{h}" radius="{r}"/>'
               '\n        </geometry>'
               '\n      </visual>'
               '\n      <collision>'
               '\n        <geometry>'
              f'\n          <cylinder length="{h}" radius="{r}"/>'
               '\n        </geometry>'
               '\n      </collision>'
               '\n    </link>\n')  
    def ask_continue():
        global ask
        while True:
            ask = input("Do you want to quit, then answer yes if you want to continue answer no: ")
            if ask in ["yes","no"]:
                break
            else:
                print("Not a valid answer, try again.")
    def save_file():
        while True:
            file_name = input("give a filename where to save, use .xml ending for filename: ")
            if file_name.endswith(".xml"):
                break
            else:
                print("again with ending is .xml")
        with open(file_name,"a") as file:
            file.write(text_1)
    def main():
        if __name__ == "__main__":
            Test.text()
            while True:
                Test.ask_link_name()
                Test.ask_shape()
                if shape == "1":
                    Test.shape_1()
                elif shape == "2":
                    Test.shape_2()
                elif shape == "3":
                    Test.shape_3()
                Test.ask_continue()
                if ask == "yes":
                    break
                elif ask == "no":
                    pass
            Test.save_file()
Test.main()
