#----------------------sets{}--------------------
'''numbers = {10,11,12,13}

for num in numbers:
    print(num)



# Creating a set
set = {1,2,3,4,6,5,6,7,8,9}

print(set)
#Addingan an Elements to a Set
set.add(5)
print(set)

#Removing an Elements from a Set
set.remove(5)
print(set)
set.remove(4)
print(set)
#discard an element from a set
set.discard(2)
print(set)
#pop a element
set.pop()
print(set)
#Set Operations (Union, Intersection, Difference, Symmetric Difference)
set1 = {1,2,3,4}
set2= {4,5,6,1}
print(set1 | set2) # will get all values without repeat
print(set1 & set2) # will get only repeated values
print(set1 - set2) # will get only unique elements in set1 only
print(set2-set1) # will get only unique elemetns in set2 only
print(set1 ^ set2) # will get non repeated values


#Checking for Element Existence
print(3 in set1)

# Iterating Through a Set
set = {1,2,3,4,5,6,7,8,99}
for num in set:
    print(num)

fruits = {'Apple','Banana','Orange'}
for item in fruits:
    print(item)

#Finding Length of a Set
print(len(set))
'''
# Converting List to Set (Removing Duplicates)
l100 = [12,12,12,13,14,14,16,16,15,17]
new_set = set(l100)
print(new_set)
  # Converts list to set, removing duplicates

#Set Subset and Superset
seta = {1,2,3,4}
setb = {1,2,3,4,5,6}
print(seta.issubset(setb))
print(setb.issubset(seta))

#Frozen Set (Immutable Set)
fset =frozenset([1,2,3,4,5])
print(fset)

seta.add(5)
print(seta)

frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})


#-----------------------DICTIONARY--------------------------------------------------------------

#1. Create and Print a Dictionary
"""names = {
    "Manju":"RG mega",
    "Sateesh":"SVN2",
    "Manoj":"SVN3",
    "Naresh":"Veejay",
    "Guna":"VYjanthi"
}

print(names)"""
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