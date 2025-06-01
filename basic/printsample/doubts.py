
squares = {x:x**2  for x in range(10)}
print(squares)

#8. Count Word Frequencies
text = "apple banana apple orange banana apple"
words = text.split()

# Count frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


#9. Sort a Dictionary by Keys or Values
# Sort by keys
sorted_by_keys = dict(sorted(squares.items()))
print(sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(squares.items(), key=lambda item: item[1]))
print(sorted_by_values)

#10 Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

print(nested_dict["person1"]["name"])  # Output: Alice

'''
# 1. Check if a number is a whole number
def is_whole_number(n):
    return n >= 0 and isinstance(n, int) #If we remove from isinstance(n,int) we are getting o/p else not remove


num = int(input("Enter a number: "))
if is_whole_number(num):
    print(f"{num} is a whole number.")
else:
    print(f"{num} is not a whole number.")
'''


#5. Checking If a Number is Float
def is_float(value):
    return isinstance(value,float)

print("Entered value is a float : " , is_float(55.87))


#10. Comparing Floating-Point Numbers Using math.isclose()

import math

a = 0.1 + 0.2
b = 0.3

print(math.isclose(a, b, rel_tol=1e-9))  # True (compares within a small tolerance)

#Example 1: Using sort()

number = [42,12,52,3,55]
number.sort()
print(number)
print(number.sort())