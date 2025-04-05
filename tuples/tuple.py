# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple with one item
thistuple = ("apple",)
print(thistuple)  # Output: ('apple',)

# Tuple with different data types
thistuple = ("apple", 1, True)
print(thistuple)  # Output: ('apple', 1, True)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Accessing Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Output: banana
print(thistuple[-1])  # Output: cherry
print(thistuple[1:3])  # Output: ('banana', 'cherry')
print(thistuple[:2])  # Output: ('apple', 'banana')
print(thistuple[1:])  # Output: ('banana', 'cherry')


# Checking if Item Exists
thistuple = ("apple", "banana", "cherry")
if "banana" in thistuple:
    print("Yes, 'banana' is in the fruits tuple")  # Output: Yes, 'banana' is in the fruits tuple


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')
mylist = list(thistuple)  # convert to list
mylist[1] = "kiwi"  # change the value
thistuple = tuple(mylist)  # convert back to tuple
print(thistuple)  # Output: ('apple', 'kiwi', 'cherry')


# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# But there is a workaround. You can convert the tuple into a list, add the item, and convert it back into a tuple. 
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')
mylist = list(thistuple)  # convert to list
mylist.append("orange")  # add item
thistuple = tuple(mylist)  # convert back to tuple
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')


# Remove Items
# Once a tuple is created, you cannot remove items from it. Tuples are unchangeable.
# But there is a workaround. You can convert the tuple into a list, remove the item, and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')
mylist = list(thistuple)  # convert to list
mylist.remove("banana")  # remove item
thistuple = tuple(mylist)  # convert back to tuple
print(thistuple)  # Output: ('apple', 'cherry')


# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking" a tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')
apple, banana, cherry = thistuple  # unpacking
print(apple)  # Output: apple

myTuple = ("apple", "banana", "cherry")
mySecondTuple = (1, 2, 3)
myThirdTuple = (True, False, True)

myFourthTuple = (myTuple, mySecondTuple, myThirdTuple)  # nested tuple
print(myFourthTuple)  # Output: (('apple', 'banana', 'cherry'), (1, 2, 3), (True, False, True))
print(myFourthTuple[0])  # Output: ('apple', 'banana', 'cherry')
print(myFourthTuple[0][1])  # Output: banana
print(myFourthTuple[1][2])  # Output: 3

myFourthTuple = myTuple + mySecondTuple + myThirdTuple  # concatenation
print(myFourthTuple)  # Output: ('apple', 'banana', 'cherry', 1, 2, 3, True, False, True)
print(myFourthTuple.count("apple"))  # Output: 1
print(myFourthTuple.count(1))  # Output: 1
print(myFourthTuple.count(True))  # Output: 2
print(myFourthTuple[4]) # Output: 2


# unpacking
(first, second, *rest) = myFourthTuple  
print(first)  # Output: apple
print(second)  # Output: banana
print(rest)  # Output: ['cherry', 1, 2, 3, True, False, True]
print(rest[0])  # Output: cherry
print(rest[1])  # Output: 1

(first, *rest, last) = myFourthTuple
print(first)  # Output: apple
print(last)  # Output: True
print(rest)  # Output: ['banana', 'cherry', 1, 2, 3, True, False]


# Looping Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)  # Output: apple banana cherry


# Looping Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])  # Output: apple banana cherry
