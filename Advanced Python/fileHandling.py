# File Handling with Python

# Creating a file
'''
try:
    file = open("./Advanced Python/new_file.txt", "x")
    file.write("This is a new file.")
except FileExistsError as error:
    print(error)
finally:
    try:
        file.close()
    except:
        print("File already exists.")
'''

# method - readline() and readlines()
# readline(optional arg int) -> reads single line from the file. The argument defines the number of characters to read from the line.
'''
try: 
    file = open("./Advanced Python/new_file.txt", "r")
    print(file.readline())
    print(file.readline(10))
except:
    print("File not found.")
finally:
    file.close()
'''

# readlines() - makes a list of list of lines of the file content
try: 
    file = open("./Advanced Python/new_file.txt", "r")
    for line in file.readlines():
        print(line)
except:
    print("File not found.")
finally:
    file.close()