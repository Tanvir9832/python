
# declare sets
thisset = {"apple", "banana", "cherry", "apple", True, False, 1, 0, 3}
print(thisset) 
# duplicates are ignored 
# False and 0 is considered the same value  # True and 1 is considered the same value
# output: {'banana', True, False, 3, 'cherry', 'apple'}


# set constructor
thisset = set(("apple", "banana", "cherry", "apple", True, False, 1, 0, 3))
print(thisset) # duplicates are ignored


# adding elements to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.add("apple") # duplicates are ignored
print(thisset) # output: {'banana', 'orange', 'cherry', 'apple'}

# adding multiple elements to a set
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset) # output: {'banana', 'orange', 'grapes', 'cherry', 'apple', 'mango'}

# adding multiple elements to a set using union
thisset = {"apple", "banana", "cherry"}
thisset.update({"orange", "mango", "grapes"})
print(thisset) # output: {'banana', 'orange', 'grapes', 'cherry', 'apple', 'mango'}

# adding multiple elements to a set using union operator
thisset = {"apple", "banana", "cherry"}
thisset = thisset.union({"orange", "mango", "grapes"})
print(thisset) # output: {'banana', 'orange', 'grapes', 'cherry', 'apple', 'mango'}

# removing elements from a set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # output: {'cherry', 'apple'}
# thisset.remove("banana") # raises KeyError if the element is not found
thisset.discard("apple")
print(thisset) # output: {'cherry'}

thisset.pop() # removes the last element from the set
print(thisset) # output: {'banana', 'cherry'}


thisset.add("banana") 
thisset.add("cherry")
print(thisset) # output: {'banana', 'cherry'}
thisset.clear() # removes all elements from the set
print(thisset) # output: set()
thisset = {"apple", "banana", "cherry"}
# del thisset # deletes the set
# print(thisset) # raises NameError: name 'thisset' is not defined




# set operations
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.union(set2) # union of two sets
print(set3) # output: {'banana', 'google', 'apple', 'microsoft', 'cherry'}

set3 = set1 | set2 # union of two sets using operator
print(set3) # output: {'banana', 'google', 'apple', 'microsoft', 'cherry'}
set3 = set1.intersection(set2) # intersection of two sets   
print(set3) # output: {'apple'}
set3 = set1 & set2 # intersection of two sets using operator
print(set3) # output: {'apple'}
set3 = set1.difference(set2) # difference of two sets
print(set3) # output: {'banana', 'cherry'}
set3 = set1 - set2 # difference of two sets using operator
print(set3) # output: {'banana', 'cherry'}
set3 = set1.symmetric_difference(set2) # symmetric difference of two sets
print(set3) # output: {'banana', 'google', 'microsoft', 'cherry'}
set3 = set1 ^ set2 # symmetric difference of two sets using operator
print(set3) # output: {'banana', 'google', 'microsoft', 'cherry'}




# set comprehension
set1 = {x for x in "banana"}
print(set1) # output: {'a', 'b', 'n'}

set1 = {x for x in "banana" if x != "a"}
print(set1) # output: {'b', 'n'}



# loop through set 
for x in thisset:
    print(x) # output: apple banana cherry orange mango grapes

