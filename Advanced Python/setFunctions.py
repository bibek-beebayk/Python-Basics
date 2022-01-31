# Set() - collection of unordered unique data

# add() - adds new element to the set

fruits = {"Apple", "Orange", "Mango"}
print("Fruits: ", fruits)
fruits.add("Strawberry")
print("add(): ", fruits)

# copy() - replicates or copies all elements from the existing set to new set
fruits_box = fruits.copy()
print("Fruits Box: ", fruits_box)

# clear() - removes all elements from the set
fruits_box.clear()
print("Fruits Box: ", fruits_box)

# union() - merge all elements of two or more set and creates new set without affecting the existing sets

set_even = {0, 2, 4, 6, 8}
set_odd = {1,3,5,7,9}
print("Set Even: ", set_even)
print("Set Odd: ", set_odd)
set_whole_number = set_even.union(set_odd)
print("Union: ", set_whole_number)
print("Set Even: ", set_even)
print("Set Odd: ", set_odd)

# update() - updates the elemet of set
set_movie = {"Spider Man", "Avengers", "Constantine"}
print("Original Set Movie: ", set_movie)
set_update = {"Dr. Strange", "Inception"}
set_movie.update(set_update)
print("Set Update: ", set_update)
print("Updated Set Movie: ", set_movie)

# set() - change to set
gender = ["Male", "Female", "Other"]
set_gender = set(gender)
print("Gender List: ", gender)
print("Gender Set: ", set_gender)

# difference() - calculates the difference of the two sets and returns it; doesn't affect the original sets
set_a = {0,2,4,6,8}
set_b = {1,2,3,4,5,6,7,8,9}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Difference (B-A): ", set_b.difference(set_a))

# difference_update() - removes all matched elements and keeps unmatched elements in the primary set
set_a = {0,2,4,6,8}
set_b = {1,2,3,4,5,6,7,8,9}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Difference (B-A): ", set_b.difference_update(set_a))
print("Set A: ", set_a)
print("Set B: ", set_b)

# symmetric_difference() - returns the remaining values from both the sets
print("\n***** symmetric_difference() ******\n")
set_a = {0,2,4,6,8}
set_b = {1,3,5,7,9}
set_c = {0,1,2,3,4,5,6,7,8,9}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Set c: ", set_c)
print("Symmetric Difference of A and C: ", set_a.symmetric_difference(set_c))
print("Symmetric Difference of A and b: ", set_a.symmetric_difference(set_b))
print("Symmetric Difference of b and C: ", set_b.symmetric_difference(set_c))
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Set c: ", set_c)

# symmetric_difference_update()
print("\n***** symmetric_difference_update() ******\n")
set_a = {0,2,4,6,8}
set_b = {1,3,5,7,9}
set_c = {0,1,2,3,4,5,6,7,8,9}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Set c: ", set_c)
print("Symmetric Difference of A and C: ", set_a.symmetric_difference_update(set_c))
print("Set A: ", set_a)
print("Symmetric Difference of A and b: ", set_a.symmetric_difference_update(set_b))
print("Set A: ", set_a)

print("Symmetric Difference of b and C: ", set_b.symmetric_difference_update(set_c))

print("Set A: ", set_a)
print("Set B: ", set_b)
print("Set C: ", set_c)

# intersection() -> returns the intersection of two sets
print("\n****** intersection() ******")
set_a = {1,2,3,4,5,6,7}
set_b = {5,6,7,8,9,0}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Intersection of A and B: ", set_a.intersection(set_b))

# intersection_update() -> updates the primary set with the intersection value
print("\n****** intersection_update() ******")
set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Intersection of A and B: ", set_a.intersection_update(set_b))
print("Set A: ", set_a)
print("Set B: ", set_b)

# pop() -> removes an arbitrary value from the set; raises keyerror if the set is empty
print("\n****** pop() ******")
fruits_set = {"apple", "mango", "grapes", "avocado", "litchi"}
print("Original set: ", fruits_set)
fruits_set.pop()
print("After popping: ", fruits_set)
fruits_set.pop()
print("After popping: ", fruits_set)
fruits_set.pop()
print("After popping: ", fruits_set)
fruits_set.pop()
print("After popping: ", fruits_set)
fruits_set.pop()
print("After popping: ", fruits_set)
# fruits_set.pop()
# print("After popping: ", fruits_set)

# remove() -> removes an item from the set and returns keyerror if the key is not found
print("\n****** remove() ******")
fruits_set = {"apple", "mango", "grapes", "avocado", "litchi"}
print("Original set: ", fruits_set)
fruits_set.remove("apple")
print("After removing: ", fruits_set)


# discard() -> remove specified element; no error if the item is not found
print("\n****** discard() ******")
fruits_set = {"apple", "mango", "grapes", "avocado", "litchi"}
print("Original set: ", fruits_set)
fruits_set.discard("apple")
print("After removing: ", fruits_set)
fruits_set.discard("apple")
print("After removing: ", fruits_set)

# isdisjoint() -> returns true if the sets are disjoint, else returns false
set_a = {1,2,3,4,5}
set_b = {6,7,8,9,0}
set_c = {4,5,6,7,8}
print(set_a.isdisjoint(set_b))
print(set_a.isdisjoint(set_c))

# issuperset() -> returns true if set is the superset of another set
# issubset()
set_a = {1,2,3,4,5,6,7}
set_b = {2,3,4,5}
print(set_a.issuperset(set_b)) # true
print(set_a.issubset(set_b)) # false
print(set_b.issubset(set_a)) # true

