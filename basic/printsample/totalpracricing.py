num = int(input("Enter a value :"))

if num %2==0:
    print(f" The entered number {num } is a even number")
else:
    print("The entered number %s is not an even number".format(num))


#2. Find Even Numbers in a List
list = [20,43,55,12,25,532,89,90]

even_num = [num for num in list if num%2==0]
print("The even numbers are :",even_num)

#3. Find Even Numbers in a Tuple

tuple_numbers = (12,242,4632,3742,2,23423,6324,23,252,64,6,544,6,89)
even_in_tuples = tuple(num for num in tuple_numbers if num%2==0)
print(tuple_numbers)
print(f"The even numbers are in tuples are : {even_in_tuples}")


#4. Filter Even Numbers from a Set

sets = {22,44,34,43,54,65,78,9909,81,43,56,76,78,78,98,13,15,75}
sets_even = {num for num in sets if num%2 ==0}
print(f"The even numbers in set are : {sets_even}")

#5. Extract Even Numbers from a Dictionary

dict = dict(a =6,b=4,c=23,d=12,e=31,p=66)
even_dict = {key:values for key, values in dict.items() if values %2==0}
print(even_dict)