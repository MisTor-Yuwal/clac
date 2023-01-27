import math
ar = "Arthimatic"
ad = "addition"
m = "multiplication"
tr = "trigonometry"
anr = "angle and radian"
r = "radian"
an = "angle"
sq = "square root"

x = input("what type of operation do you want to execute:\t")

# arthimatic operation's

if x == 'ar' or x == 'AR':
    y = input("which Arthimatic operation do you wanna execute?: ")
    if y == 'ad' or y == 'A':
        def add(first_num, second_num):
            addition = first_num + second_num
            return addition
        m = float(input("first number: "))
        n = float(input("second number: "))
        print(add(m,n))
    elif y == 'm' or y == 'M':
        def mul(first_number,second_number):
            multiplication = first_number * second_number
            return multiplication
        m = float(input("first number: "))
        n = float(input("second number: "))
        print(mul(n,m))
    elif y == 'sq' or y == 'SQ':
        def square_root(value):
            square = math.sqrt(value)
            return square
        v = float(input("value: "))
        print(square_root(v))

# trigonometric operation
# just a simple coding/ defining function for every fucking operation like amature

elif x == 'tr' or x == 'TR':
    z = input("type of trigonometric operation you wanna execute?: ")
    if z == 'sin' or z == 'S':
        def Trigonometric_opertaion_sin(value):
            sin = math.sin(value)
            return sin
        v = float(input("value: "))
        print(Trigonometric_opertaion_sin(v))
    elif z == 'cos' or z == 'C':
        def Trigonometric_operation_cos(value):
            cos = math.cos(value)
            return cos
        v = float(input("value: "))
        print(Trigonometric_operation_cos(v))
    elif z == 'tan' or z == 'T':
        def Trigonometric_operation_tan(value):
            tan = math.tan(value)
            return tan
        v = float(input("value: "))
        print(Trigonometric_operation_tan(v))

# angles and radian

elif x == 'anr' or x == 'ANR': 
    print("convert radian/angle to angle/radian")
    option = input("radian or angle: ")
    if option == 'r' or option =='R':
        def angel(value):
            radian_to_angle = math.degrees(value)
            return radian_to_angle
        v = float(input("enter value: "))
        print(angel(v))
    elif option == 'an' or option == 'AN':
        def radian(value):
            angle_to_radian = math.radians(value)
            return angle_to_radian
        v = float(input("value: "))
        print(radian(v))
    else:
        print("default")
else:
    print("default")
