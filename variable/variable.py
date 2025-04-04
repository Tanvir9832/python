

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