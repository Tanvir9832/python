# list diclaration
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(type(mylist))

# list size
print(len(mylist))

#loop through a list
for x in mylist:
    print(x)

# check if item exists in list
if "banana" in mylist:
    print("Yes, 'banana' is in the fruits list")


# list index
print(mylist[1])  # banana
print(mylist[0])  # apple
print(mylist[-1])  # cherry
print(mylist[-2])  # banana

# list slicing
print(mylist[1:3])  # banana, cherry
print(mylist[:2])  # apple, banana
print(mylist[1:])  # banana, cherry
print(mylist[-2:])  # banana, cherry
print(mylist[1:-1])  # banana, cherry


### list methods

# append() method
mylist.append("orange")
print(mylist)  # apple, banana, cherry, orange

# insert() method
mylist.insert(1, "orange")
print(mylist)  # apple, orange, banana, cherry, orange

# extend() method
mylist.extend(["kiwi", "mango"])
print(mylist)  # apple, orange, banana, cherry, orange, kiwi, mango

mylist2 = ["kiwi", "mango", "pineapple"]
mylist.extend(mylist2)
print(mylist)  # apple, orange, banana, cherry, orange, kiwi, mango, pineapple  


# remove() method
mylist.remove("banana")
print(mylist)  # apple, orange, cherry, orange, kiwi, mango, pineapple

# pop() method
mylist.pop()  # removes the last item
print(mylist)  # apple, orange, cherry, orange, kiwi, mango, pineapple

mylist.pop(1)  # removes the item at index 1
print(mylist)  # apple, cherry, orange, kiwi, mango, pineapple

#del method
del mylist[1]  # removes the item at index 1
print(mylist)  # apple, orange, kiwi, mango, pineapple

# clear() method
mylist.clear()  # removes all items in the list
print(mylist)  # []


# copy() method
mylist = ["apple", "banana", "cherry"]
mylist2 = mylist.copy()  # creates a copy of the list
print(mylist2)  # apple, banana, cherry

# count() method
mylist = ["apple", "banana", "cherry", "banana"]
print(mylist.count("banana"))  # 2
print(mylist.count("apple"))  # 1
print(mylist.count("kiwi"))  # 0

# index() method
mylist = ["apple", "banana", "cherry"]
print(mylist.index("banana"))  # 1
print(mylist.index("apple"))  # 0
print(mylist.index("kiwi"))  # ValueError: 'kiwi' is not in list

# sort() method
mylist = ["banana", "apple", "cherry"]
mylist.sort()  # sorts the list in ascending order
print(mylist)  # apple, banana, cherry
# reverse sort
mylist.sort(reverse=True)  # sorts the list in descending order
print(mylist)  # cherry, banana, apple

# reverse() method
mylist.reverse()  # reverses the order of the list
print(mylist)  # apple, banana, cherry



mylist = mylist + mylist
print(mylist)  # apple, banana, cherry, apple, banana, cherry
print(mylist * 2)  # apple, banana, cherry, apple, banana, cherry, apple, banana, cherry, apple, banana, cherry