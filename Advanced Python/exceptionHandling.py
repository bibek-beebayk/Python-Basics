# Exception Handling - to handle compilation error within the program

# error may occur due to
# 1. user input
# 2. calculation
# 3. memory
# and so on

# Types of Exception or Error in Python
# 1. KeyError
# 2. ValueError
# 3. NameError
# 4. SystemError
# 5. ZeroDivisionError
# 6. MemoryOverFlow
# 7. UnicodeTranslateError
# 8. SyntaxError
# 9. RuntimeError
# 10. SystemExit
# 11. IndexError

# code without exception handling

name_list = ["Sajan", "Himal", "Bimala", "Madhu", "Bibash"]
print(name_list.index("Himal"))
print(name_list[0])
print("Hello")

# compilation error - for developer and development environment not for end-user or
# production environment

# syntax of Exception handling in Python
try:
    print(name_list[8])
    print("Block of code")
except:
    print("Message")

# syntax of Exception handling in Java
'''try {
    System.out.println(0/100);
}catch(Exception e){
    System.out.println(e.getMessage());
}'''

# keyword used in Exception Handling in Python
# 1. try - checks the block of code whether the code contains error or not
# 2. except - error handle and throws proper message
# 3. else - contains errorless block of code
# 4. finally - executes the code regardless of the error occured or not in try-except

# example of exception handling
# 1. Case one - basic
'''
try:
    num_one = int(input("Enter the first number: "))
    num_two = int(input("Enter the second number: "))
    print("Sum is: ", num_one + num_two)
except:
    print("Value must be numbers.")

print("Hello we are trying out some basic examples of Exception Handling in Python")
'''

# 2. Case two - else
'''
try:
    name = int(input("Enter an integer: "))
    print("Number = ", name)
except:
    print("Invalid Input, must be an integer")
else:
    address = "Kathmandu"
    print("Address: ", address)
'''

# 3. Case three - finally
# 4. Case four - nested try-except
try:
    f = open("C:/Users/beeba/OneDrive/Documents/Python django class/Advanced Python/abcd.txt", "r")
    print(f.read())
except:
    print("File not found.. ")
finally:
    try:
        f.close()
        print("File Closed")
    except:
        print("File not found.")


# case five - specific exception
'''
try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    print("Result of division: ", num_1/num_2)
except ZeroDivisionError:
    print("Second number must not be zero.")
'''

# 6. Case six - specific exception with other exceptions
'''
try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    print("Result of division: ", num_1/num_2)
except ZeroDivisionError:
    print("Second number must not be zero.")
except:
    print("Must be numeric values.")

'''

# 7. case seven - specific exception with message
try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    print("Result of division: ", num_1/num_2)
except ZeroDivisionError as error:
    print(error)
except:
    print("Must be numeric values.")

# 8. case eight - multiple specific exceptions
