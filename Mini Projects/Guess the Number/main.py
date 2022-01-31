import random

num1 = random.randint(1,89)
num2 = num1 + 10


number = random.randint(num1,num2)


def generate_hint(num):
    multiplier = random.randint(1,20);
    # print(multiplier)

    incrementor = random.randint(1,30);
    # print(incrementor)
    hint_num = (num * multiplier + incrementor)
    return(f"({hint_num}-{incrementor})/{multiplier}")


# print(number)

print(f"Guess a number within {num1} and {num2}.")
print("Your hint: ", generate_hint(number))

def test_guessed_number():
    try:
        num = int(input("Enter your guess: "))
    except:
        print("Input Error. Input not an integer.")
        return
    
    if num > num2 or num < num1:
        print("Your guess should be within {num1} and {num2}.")
        return
    return num



guessed_number = test_guessed_number()
    



def test_guess(number, guess):
    if guess:
        if guess == number:
            print("Congratulations! You made the correct guess.")
            print(f"Your Guess: {guess}")
            print(f"The number: {number}")
        else:
            print("Sorry! Your guess is wrong.")
            print(f"Your Guess: {guess}")
            print(f"The number: {number}")

test_guess(number, guessed_number )