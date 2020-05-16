# This is to introduce the datatypes used in Python.
# In Python - we have the following datatypes:
# Here, I have tried variable names using best practices and rules (following PEP 8)

# Integers: int
_price = 120
print("integer value, price : ")
print(_price)
# To get the dataType of variable
type(_price)
print("")

# Floating point: float
_price = 120.0
print("Floating point value, price : ")
print(_price)
# To get the dataType of variable
type(_price)
print("")

# Strings: str
_greeting = "I'm loving it!"
print("String in the from of greeting")
print(_greeting)
# To get the dataType of variable
type(_greeting)
print("")

# Lists: list (ordered sequence of objects)
_price_list = [12.0, 15.0, 20.0]
print("Lists example - ordered sequence of objects")
print(_price_list)
# To get the dataType of variable
type(_price_list)
print("")

# Dictionaries: dict (Unordered key/value pairs)
_unordered_dict = {"first_name":"Ritendra", "last_name":"Singh"}
print("Dictionary example - Unordered key/value pairs!")
print(_unordered_dict)
# To get the dataType of variable
type(_unordered_dict)
print("")

# Tuples: tup (ordered immutable sequence of objects)
_tuple_list = [10.0, "Hello", 20.0]
print("Tuples example - ordered immutable sequence of objects!")
print(_tuple_list)
# To get the dataType of variable
type(_tuple_list)
print("")

# Sets: set (Unordered collection of unique objects)
_sets_variable = {"a", "b", "c", "d", "e"}
print("Sets example - Unordered collection of unique objects!")
print(_sets_variable)
# To get the dataType of variable
type(_sets_variable)
print("")

# Booleans: bool
_is_python_good = True
print("Boolean example")
print(_is_python_good)
# To get the dataType of variable
type(_is_python_good)
