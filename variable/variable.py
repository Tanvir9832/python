

# variable 
x = 5
y = "tanvir"

print(x) # 5
print(y) # tanvir

X = 10
print(X) # 10
print(x) # 5


# many values to multiple variables
a, b, c = "tanvir", 1, 2.5
print(a) # tanvir
print(b) # 1
print(c) # 2.5

# One Value to Multiple Variables
a = b = c = "tanvir"
print(a) # tanvir
print(b) # tanvir
print(c) # tanvir

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry

# Global Variables
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x) # Python is fantastic




# String Variables


# String variables can be declared either by single or double quotes

random_string = "Hello World"
print(random_string) # Hello World

# String variables can also be declared using triple quotes
random_string = '''Hello World'''
print(random_string) # Hello World
random_string = """Hello World   """
print(random_string) # Hello World

# String Length
print(len(random_string)) # 11

# String Quotes
print("I'm Tanvir") # I'm Tanvir
print('I\'m Tanvir') # I'm Tanvir
print("I\"m Tanvir") # I'm Tanvir

# String Slicing
print(random_string[0]) # H
print(random_string[1]) # e
print(random_string[2]) # l
print(random_string[1:3]) # el
print(random_string[2:5]) # llo
print(random_string[2:]) # llo World
print(random_string[:5]) # Hello
print(random_string[-1]) # d
print(random_string[-2]) # l


# String Methods
print(random_string.upper()) # HELLO WORLD
print(random_string.lower()) # hello world
print(random_string.strip()) # Hello World (removes whitespace)
print(random_string.replace("H", "J")) # Jello World
print(random_string.split(" ")) # ['Hello', 'World'] (returns a list)
print(random_string.split(",")) # ['Hello World'] (returns a list)


# String Concatenation
print("Hello" + " World") # Hello World
print("Hello" + " " + "World") # Hello World
print("Hello" + " " + "World" + "!") # Hello World!


# String Formatting
name = "Tanvir"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.") # My name is Tanvir and I am 25 years old.
print("My name is {} and I am {} years old.".format(name, age)) # My name is Tanvir and I am 25 years old.
print(f"My name is {name} and I am {age} years old.") # My name is Tanvir and I am 25 years old.
print("My name is %s and I am %d years old." % (name, age)) # My name is Tanvir and I am 25 years old.
print("My name is {0} and I am {1} years old.".format(name, age)) # My name is Tanvir and I am 25 years old.
print("My name is {name} and I am {age} years old.".format(name=name, age=age)) # My name is Tanvir and I am 25 years old.
print("My name is {0} and I am {1} years old.".format(name, age)) # My name is Tanvir and I am 25 years old.


# String Escape Characters
print("Hello\nWorld") # Hello World (newline)
print("Hello\tWorld") # Hello World (tab)
print("Hello\bWorld") # HelloWorld (backspace)
print("Hello\\World") # Hello\World (backslash)
print("Hello\'World") # Hello'World (single quote)


# String Indexing
print(random_string[0]) # H
print(random_string[1]) # e


# String Iteration
for x in random_string:
  print(x) # H e l l o   W o r l d


# String Membership
print("H" in random_string) # True
print("h" in random_string) # False
print("Hello" in random_string) # True



# String Count
print(random_string.count("l")) # 3
#String Find
print(random_string.find("l")) # 2
print(random_string.find("L")) # -1 (not found)
# String Index
print(random_string.index("l")) # 2
print(random_string.index("L")) # ValueError: substring not found
# String Isalnum
print(random_string.isalnum()) # False (contains space)
print("Hello123".isalnum()) # True (contains letters and numbers)
# String Isalpha
print(random_string.isalpha()) # False (contains space)
print("Hello".isalpha()) # True (contains only letters)
# String Isdigit
print(random_string.isdigit()) # False (contains letters and space)
print("123".isdigit()) # True (contains only digits)
# String Islower
print(random_string.islower()) # False (contains uppercase letters)
print("hello".islower()) # True (contains only lowercase letters)
