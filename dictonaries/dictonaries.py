
# declare a dictionary with the following keys and values:
thisDictionary = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
    },
    "hobbies": None
}

print(thisDictionary["name"])  # Output: John Doe
print(thisDictionary["age"])  # Output: 30
print(thisDictionary["city"])  # Output: New York
print(thisDictionary["is_student"])  # Output: False
print(thisDictionary["courses"])  # Output: ['Math', 'Science', 'History']
print(thisDictionary["address"]["street"])  # Output: 123 Main St


# length of the dictionary
print(len(thisDictionary))  # Output: 7

x = thisDictionary.keys()  # Get the keys of the dictionary
print(x)  # Output: dict_keys(['name', 'age', 'city', 'is_student', 'courses', 'address', 'hobbies'])

y = thisDictionary.values()  # Get the values of the dictionary
print(y)  # Output: dict_values(['John Doe', 30, 'New York', False, ['Math', 'Science', 'History'], {'street': '123 Main St', 'zipcode': '10001'}, None])

thisDictionary["university"] = "MIT"  # Add a new key-value pair to the dictionary
print(thisDictionary)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York', 'is_student': False, 'courses': ['Math', 'Science', 'History'], 'address': {'street': '123 Main St', 'zipcode': '10001'}, 'hobbies': None, 'university': 'MIT'}


# popItem() method removes the specified item from the dictionary
thisDictionary.pop("hobbies")  # Remove the key "hobbies" from the dictionary
print(thisDictionary)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York', 'is_student': False, 'courses': ['Math', 'Science', 'History'], 'address': {'street': '123 Main St', 'zipcode': '10001'}, 'university': 'MIT'}

thisDictionary.popitem()  # Remove the last inserted item from the dictionary
print(thisDictionary)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York', 'is_student': False, 'courses': ['Math', 'Science', 'History'], 'address': {'street': '123 Main St', 'zipcode': '10001'}}


