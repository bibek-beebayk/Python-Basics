# List
# 1. copy() - replicates or dubilcates all
# items of the primary list to new list
# we target

book_names = ["Macbed", "Hamlet", \
              "Game of Thrones", \
              "Mahabharat", "Muna Madan", \
              "Seto Bagh"]
print("Books' name before: ", book_names, "\n")
book_names_copy = book_names.copy()
print("Copy list: ", book_names_copy, "\n")

# 2. append() - takes single item (string) as param
# adds new item at last index of list
book_names.append("The last samurai")
book_names.append("Seto Surya")
print("Appended list: ", book_names, "\n")

extra_books = ["Java", "JS", "Python"]

for book in extra_books:
    book_names.append(book)
else:
    print("No more books to add")
print("Appended list with loop: ", book_names, "\n")

# 3. extend() - takes single list (iterable object)
# as param and adds param list's items
# to the primary list items

political_science = ["Mafia", "Chor", "Khate"]
book_names.extend(political_science)
print("Extended book list: ", book_names, "\n")

# 4. insert()
# takes two param
# i. index number
# ii. object (string, list)
# adds the item or object to the targeted
# index of the primary list

book_names.insert(4, "Hellen Keller")
print("Inserted book list: ", book_names, "\n")

book_names.insert(15, "Killer Pasha")
print("Inserted book list: ", book_names, "\n")

# 5. clear() - removes all the items
# from the list
print("Book copied list: ", book_names_copy, "\n")
book_names_copy.clear()
print("Book cleared list: ", book_names_copy, "\n")

# 6. pop() - removes the targeted item from the
# list of index and return its value

# case one : pop() - pop default - no param
# removes the last index item
print(book_names.pop())
print("Book pop default", book_names, "\n")
# case two: pop(x) - pop index - takes index as param
# removes the targeted index item
print(book_names.pop(5))
print("Book pop index", book_names, "\n")

# note:- if the index is not found then
# throws IndexError

# 7. remove()
# takes object's value as param * return value
# after removing the item from the list
# throws ValueError if the item is not available
print(book_names.remove("Mafia"))
print("Book pop index", book_names, "\n")

# all types of data passed in the remove method
# are considered as value not index by the
# remove method

# 8. count() - takes value as param and counts
# the number of value present in the list
x = [2, 2, 4, 5, 11, 23, 2, 44]
print(x.count(2))

# throws error if the param is missing
# print(x.count())

# 9. reverse() - shuffle the list and place
# item starting from last index to start index

numbers = [0, 1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers)

# 10. sort() - sorts or organized items in list
# in ascending order
numbers.sort()

print(numbers)
