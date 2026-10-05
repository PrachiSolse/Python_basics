#Python supports several built-in data types:

#Integers (int): Whole numbers (e.g., 10, -5).
#Floats (float): Decimal numbers (e.g., 3.14, -0.001).
#Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
#Booleans (bool): Represents True or False.
#Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
#Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
#Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
#Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).


age=22                                # integer
cgpa=9.2                              # float
name="Prachi"                         # string
is_present=True                       # Boolean
items=["apple","mango",34,9.4,True]   # list
t=(1,4,"apple")                       #tuple
s={1,2,4,6,4,3}                       #sets
d={name:"Prachi", age:22}             #dictionaries



#Checking Data Types
#Use the type() function to check the data type of a variable.
print(type(10))       # Output: <class 'int'>
print(type("Hello"))  # Output: <class 'str'>