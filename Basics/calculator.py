# Case Study covering functions, if-else, operators

def mycalc_add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1+num2;

def mycalc_subtract():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1-num2;

def mycalc_multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1*num2;

def mycalc_divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1/num2;


def start_calculator(key):
    if key == "k":
        print(message("wc"))
        print(message("action"))
        command = input("Enter key command as suggested: ")
        if command == "A":
            print(mycalc_add())
            
            start_calculator("k")
            print(message("action"))
        elif command == "S":
            print(mycalc_subtract())
            start_calculator("k")
            print(message("action"))
        elif command == "M":
            print(mycalc_multiply())
            start_calculator("k")
            print(message("action"))
        elif command == "D":
            print(mycalc_divide())
            start_calculator("k")
            print(message("action"))
        else:
            print(message("keyerror"))
            
    elif key == "c":
        print(message("cl"))
    elif key == "r":
        print(message("action"))
        start_calculator("k")
    else:
        print("No key selected")

def message(msg):
    if msg == "error":
        return "Something went wrong."
    elif msg == "wc":
        return "Welcome to My Calculator"
    elif msg == "cl":
        return "Thank You"
    elif msg == "st":
        return "My Calculator 2022"
    elif msg == "cfm":
        return "Type:- \n1. K to Start\n2. C to Close"
    elif msg=="action":
        return "Type:-\n1. A to add\n2. S to subtract\n3. M to Multiply\n4. D to Divide"
    elif msg == "keyerror":
        return("Invalid Key")
    else:
        return "No Response"

print(message("st"))
print(message("cfm"))
print(message("action"))
key = input("Enter key to start: ")
start_calculator(key)
