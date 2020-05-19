# This file contains some operations on strings(Indexing and Slicing). We use incex here, starting from 0.
#

_string = "India is a great country!"

# Slice string and print "India".
print(_string[:5])

# Slice string and print text after "India"
print(_string[5:])

# print only "great" from the string
print(_string[11:16])

# print full string - in colon notation
print(_string[::])

# print string by skipping characters - step-size: 2
# start : stop : step-size
print(_string[::2])

# print string by skipping characters - providing start, stop and step-size
# start : stop : step-size
print(_string[0:15:2])

# reverse string - Python trick
print(_string[::-1])

# Print "r" from the string "Hello World"
_string = "Hello World"
print(_string[8:9])

# Print "ink" from the string "tinker"
print('tinker'[1:4])

# String concatenation
_string_1 = "Hello"
_string_2 = "World!"
_string_concatenated = _string_1 + _string_2
print(_string_concatenated)
print('')

# String multiplication
_string_m = "Hello"
print(_string_m * 5)

#String uppercase
print(_string_m.upper())

#String add - concatenate two strings
print(_string_m.__add__(_string_m))

#String split - It splits based on the whitespace by default
_string_var = "Hi, I am working as a developer!"
print(_string_var.split())

print(_string_var.split("am"))
