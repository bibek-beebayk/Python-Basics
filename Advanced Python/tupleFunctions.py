# Tuple Functions

'''
name = "Bibek" -> treated as a string
name = "Bibek", -> treated as a tuple
name = ("Bibek") -> treatde as a string
name = ("Bibek",) -> treaded as a tuple
'''

# 1. count() -> counts the number of tuple items

gender = ("Male", "Female", "Others")
print("Count:", gender.count("Male"))

# 2. index()
print("Index:", gender.index("Female"))