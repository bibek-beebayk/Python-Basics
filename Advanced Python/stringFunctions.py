# String Methods

# 1. Capitalize : Capitalize the given string.

from random import sample


name_of_place = "lumbini - the birthplace of Gautam Buddha."
print(name_of_place.capitalize())

# 2. casefold() - to change language specific letters to their English counterpart


# center()
title = "Mind Risers"
print(title.center(50, "*"))

# count() - returns the number of specified characters in a string
print(title.count("i"))

# endswith(str) : returns true if the string ends with specified value
email = "beebayk0001@gmail.com"
print(email.endswith("@gmail.com"))

# lower() - converts the string to lower case
print(title.lower())

# upper() - converts the string to upper case
print(title.upper())

# format()
print("Hello {}, how are you? Are you {}?".format("Madan", 25))
print("Hello {name}, how are you? Are you {age}?".format(name="Madan", age=25))
print("Hello {0}, how are you? Are you {1}?".format("Bibek", 26))
print("Hello {0}, how are you? Are you {age}?".format("Bibek", age=26))

# index(str) -> prints the index of the specified string where it is first encountered
quote_of_the_day = "As you show as you reap."
print(quote_of_the_day.index('as'))
print(quote_of_the_day.index('o'))

# split(str) -> breaks down the string into multiple substrings based on the provided argument and returns a list of the substrings

string1 = "My name is Bibek. I am  CSIT student. I like python."
strings = string1.split('.')
print(strings)

# replace(oldStr, newStr) -> takes two parameters, replaces the first parameters in the string by the second parameter

str2 = "This is a cat. This is another cat."
str3 = str2.replace('This', 'That' )
print(str3)

# isalnum() -> returns true if the string is alphanumeric, returns false otherwise
sample_string = "Bibek0001"
print(sample_string.isalnum())
sample_string2 = "Bibek 0001"
print(sample_string2.isalnum())