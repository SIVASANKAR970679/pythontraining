## 2. Concatenate strings

first_name = 'Muddangula'
last_name = "Sivasankar"
full_name = first_name +" " + last_name
print("Full name : " , full_name)

#String lengh means to find the number of characters in the string is called length of a string. We use len()

print("the length of full name : " , len(full_name))

# Accessing character
#In Python, accessing individual characters in a string is straightforward using indexing. Strings are sequences of characters, and each character has a position, or index, starting from 0.
print("The first character in full name is : " ,full_name[0])
print("The 7th chracter in the full name is : ", full_name[7])

#slicing

print("The first 7 characters in full name are : " , full_name[:7])
print("The last 6 charcters inthe full name is : ", full_name[:1])

#Slicing
#In Python, string slicing allows you to extract substrings from a string by specifying a range of indices.

print("The first 7 characters in full name are : " , full_name[:7])
print("The last 6 charcters inthe full name is : ", full_name[:1])

#for changing lower to upper case we can use var.upper() and from upper to lower str.lower()
print("My name is in upper case : ", full_name.upper())
print("My name in lower case : ", full_name.lower())
''''
#if we can replace the new name or string in the old name or old string then we can wuse str.replace(old_name,"new name")
new_name= full_name.replace(full_name,"Chandana w/o Siva")
print(new_name)
'''

# Check for substring
if "Siva" in full_name:
    print("The name contains 'siva' .")

# 9. Split string into a list
split = full_name.split(" ")
print(split)

#joning
join= ".".join(full_name)
print(join)