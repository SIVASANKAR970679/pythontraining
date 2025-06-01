"""----------------WHOLE NUMBERS-------------------------"""

# Addition - 3)
# Subtraction - 1

# Multiplication - 2
# Division #1.5

# Floor Division 1

# # Modulo -3

# Powers 2 * 2 * 2 = 8

# Powers

# # Order of Operations followed in Python-105  BODMAS

# Can use parentheses to specify orders--156 12 * 13

# Let's create an object called "a" and assign it the number 5

# Adding the objects


# Reassignment

# Check

# Use A to redefine A

# Check


# Use object names to keep better track of what's going on in your code!
# Show my taxes!

#1. Check if a number is a whole number
#2. Print first n whole numbers
#3. Sum of first n whole numbers
#4. Check if number is even or odd
#5. Factorial of a whole number
#6. Count of digits in a whole number
#7. Find the largest whole number in a list
#8.Find the sum of even whole numbers up to n.
#9.Reverse the digits of a whole number.
#10.Check if a whole number is a palindrome.
#11.Print a multiplication table for a number using whole numbers

'''Floating numbers '''
"""
 1.
 Basic Float Operations
"""

# Addition
# Subtraction
# Multiplication
# Division
# Floor division (removes decimal part)
# Modulus (remainder)
# Exponentiation
# Rounds to 2 decimal places
"""
3. Converting Integer to Float and Vice Versa
"""
#Convert integer to float
# Convert float to integer (truncates decimal part)
"""
4. Using math Library for Float Operations
"""
# Rounds up (10)
# Rounds down (9)
# Square root
# Pi value
"""
5. Checking If a Number is Float
"""

"""
6. Formatting Floats in Output
"""

"""
Formatted to 2 decimal places: 123.46
Formatted to 4 decimal places: 123.4568
"""

"""
7. Handling Float Division and Precision Errors
"""

"""
8. Generating Random Float Numbers
"""
"""
9. Summing a List of Floats
"""

"""
10. Comparing Floating-Point Numbers Using math.isclose()
"""


"""
"""




#---------------------NUMERICS______________________________
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type
type(5+6j) #<class 'complex'>
type(var1) #<class 'integer'>

#find the variable types
# integer variable.

# float variable.

# complex variable.


"""#------------------strings -------------------------"""


## 2. Concatenate two strings

#String length means to find the number of characters in the string is called length of a string. We use len()

# Accessing character
#In Python, accessing individual characters in a string is straightforward using indexing. Strings are sequences of characters, and each character has a position, or index, starting from 0.

#Slicing
#In Python, string slicing allows you to extract substrings from a string by specifying a range of indices.

#for changing lower to upper case we can use var.upper() and from upper to lower str.lower()

''''
#if we can replace the new name or string in the old name or old string then we can wuse str.replace(old_name,"new name")
new_name= full_name.replace(full_name,"Chandana w/o Siva")
print(new_name)
'''
#replace

# Check for substring


# 9. Split string into a list


#--------------------LIST[]--------------------------------------------------
#joning

#Example 1: Using sort()
# Ascending order
#Descending order
#Example 2: Using sorted() - By using sorted function we can get directly in ascending order with unchange of main values
# Ascending order
#Descending order
# Original list remains unchanged
#Example: Custom Sorting with key
# List of strings
# Custom sort by length of the string - Sort by String Length
#sort by a Computed Value
# Custom sort by the remainder when divided by 10
#using sorted()
#Example: Using sorted() with a Custom Key
# Original list
# Create a new sorted list based on the square of the numbers
# Apply custom sort

#Custom Sorting for Complex Data (e.g., List of Dictionaries)
# List of dictionaries

#Assign a list to a variable named my_list

# Grab element at index 0
# Grab index 1 and everything past it
# Grab everything UP TO index 3


# Reassign
# Make the list double

#Basic List Methods
# Create a new list

# Append
# Show
# Pop off the 0 indexed item
# Assign the popped element, remember default popped index is -1


# We can use the sort method and the reverse methods to also effect your lists:
# Use reverse to reverse order (this is permanent!)
# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
#Nesting Lists
# Let's make three lists
# Make a list of lists to form a matrix
# Grab first item in matrix object
# Grab first item of the first item in the matrix object
#List Comprehensions
# Build a list comprehension by deconstructing a for loop within a []
# Let's make three lists
# Make a list of lists to form a matrix
"""
1 Create a list of 5 numbers and print the sum of all numbers.

2 Write a program to find the largest number in a list.

3 Count how many times a specific element appears in a list.

4 Remove all even numbers from a list.

Reverse a list without using the reverse() method.

"""


#-------------LIST COMPREHENDER-------------------------------------------------
#finding the squares of first 10 digits

#finding even number
#Apply a Transformation
# Double each number in a list

#4. Nested Loops in List Comprehension
# Generate all pairs (x, y) where x is from 1-3 and y is from 4-6

#GENERATING PAIRS (X,Y) WHERE x is from 1,4 and y from 5-9

#5. Flatten a Nested List

#----------------------sets{}--------------------
numbers = {10,11,12,13}

for num in numbers:
    print(num)

# Creating a set

#Addingan an Elements to a Set

#Removing an Elements from a Set

#discard an element from a set

#pop a element

#Set Operations (Union, Intersection, Difference, Symmetric Difference)



#Checking for Element Existence


# Iterating Through a Set
#Finding Length of a Set

# Converting List to Set (Removing Duplicates)
  # Converts list to set, removing duplicates

# Set Subset and Superset


#Frozen Set (Immutable Set)
# Creating a frozen set

# Trying to modify it will raise an error
# frozen.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

#-----------------------DICTIONARY--------------------------------------------------------------

#1. Create and Print a Dictionary
names = {
    "Manju":"RG mega",
    "Sateesh":"SVN2",
    "Manoj":"SVN3",
    "Naresh":"Veejay",
    "Guna":"VYjanthi"
}

print(names)
#2. Access and Modify Dictionary Elements

# Modify values
# Add a new key-value pair
#3. Iterate Through a Dictionary
# Iterate through keys
# Iterate through values
# Iterate items through key values pair
#4. Check if a Key Exists

#5 5. Dictionary Comprehension






#6. Merge Two Dictionaries


# Method 1: Using the `update()` method

# Method 2: Using dictionary unpacking (Python 3.9+)



#7. Delete Items from a Dictionary

# Remove a key-value pair
# Delete all items

'''-------------LIST COMPREHENSIONS ---------------'''
