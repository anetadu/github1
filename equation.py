import math
global _equation
global characterlist

def part1 ():
    global _equation
    global characterlist
    _equation = input("please enter an equation")
    print (_equation)
    print ("Select 1 or 2")
    print ("1. X is a number")
    print ("2. x is a range")

    mylist = list(str.replace(_equation.split('=')[1], "log", ""))
    mylist = list(str.replace(_equation.split('=')[1], "cos", ""))

    mylist = list(dict.fromkeys(mylist))
    print(mylist)
    characterlist = ""
    for i in mylist:
        if i in ["x", "y", "z"]:
            characterlist += i    
    print(characterlist)
    return _equation

def run1 (equation):
    global characterlist
    for i in characterlist:
        while True:
            Lettervalue = input("what is the value of " + i)
            if str(Lettervalue) != "":
                equation = str.replace(equation, i, "(" + Lettervalue + ")")
                break
    display(equation)

def run2 (equation):
    for i in characterlist:
        while True:
            Startvalue = int(input("what is the first value " + i))
            Endvalue = int(input("what is the end value " + i))
            for j in range(Startvalue, Endvalue + 1):
                equation2 = str.replace(equation, i, "(" + str(j) + ")")
                display(equation2)
            break

def display (equation):
    for i in ["0(","1(","2(","3(","4(","5(","6(","7(","8(","9(",")("]:
        equation = str.replace(equation, i, i[0] + "*" + i[1])
    print (equation)
    equation = (str.replace(equation, "log", "math.log"))
    equation = (str.replace(equation, "cos", "math.cos"))
    print (equation)
    output_equation = equation.split('=')
    print (output_equation[0] + " = " + str(eval(output_equation[1])))

def part2(equation):
    if int(input()) == 1:
        run1 (equation)
    else:
        run2 (equation)



#Letter = input("Please enter a letter")
#Lettervalue = input("what is the value of " + Letter)
#equation = str.replace(equation, Letter, "(" + Lettervalue + ")")

#Letter2 = input("Please enter a letter")
#Lettervalue2 = input("what is the value of " + Letter2)
#equation = str.replace(equation, Letter2, "(" + Lettervalue2 + ")")

def main ():
    while True:
        part2(part1())
        print ("1. continue")
        print ("2. no")
        if int(input("Do you want to continue?")) == 2:
            break

main()
