# Dictionary Functions

# copy() - copies all items of primary dictionary to another dictionary

book_info = {'ID':"1434", "ISBN":'BB0201', "Name": "Seto Surya"}
print("Book INfo: ", book_info)
book_info_copy = book_info.copy()
print("Book Info Copy: ", book_info_copy)

# clear() - removes all items from the dictionary
book_info_copy.clear()
print("Book INfo Copy: ", book_info_copy)

# items() - returns the key-value pair from the dictionary
print(book_info.items())

for i in book_info:
    print(i)

# keys() - returns all the keys available in the dictionary
print("Keys: ",book_info.keys())

# values() - returns all values from the dictionary
print("Values: ", book_info.values())

# get() - returns the value of the specified key, if key is not found
print("get('ID'): ", book_info.get("ID"))

# pop() - removes the targeted key-value pair from the dictionary and returns value of the key that is being removed
print("pop()", book_info.pop('ISBN'))
print(book_info)

# print(book_info.pop()) - throws error, argument is required

'''
setdefault() ->> add items in the dictionary
case one = only key
case 2 = key-value
case 3 = if the key exists
    3.1 - key only
    3.2 - key-value

'''

cart_item = {"item_id": "12", "item_title":"Woolen Scarf","item_desc":"Best Nepali Handmade Woolen Scarf for Winter"}
print("Cart Items:", cart_item)
# case 1 - if only one parameter is passed, treats the parameter as key and sets the value to None
cart_item.setdefault("item_price")
print('Cart Items:', cart_item )

# case 2- if two parameters are passed, treats the first param as key and the second as value
cart_item.setdefault("Item_location ", "Kathmandu")
print("Cart Items: ", cart_item)

# case 3 - if the key already exists, there will be no changes in the dictionary
# 1. only key is passed
cart_item.setdefault("item_price")

# update() - update the value of the target key
cart_item.update({'item_price': 345})
print(cart_item)


# fromkeys() - takes two parameters (i. iterative objects; ii. both iterative objects or non iterative objects)

details = ['name', 'contact', 'address']
item = ['Hell', 'Heaven']
name = 'Kathmandu'

result = dict.fromkeys(details, item)
print(result)

result2 = dict.fromkeys(details, name)
print(result2)