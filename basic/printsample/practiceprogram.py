#Impicity type conversion
#python converts one type to another type automatically


a=10
b=3.65
c= a+b
print(type(c))
print(c)

#Explicity conversion
#Ecplicity tye conversion means, user converts the data type of one object to required data type
a = 100
a = float(a)
print("Type of a is :" ,b,type(b))

z = 1020
z = float(z)
print("The value of z is ",type(z))

# conversion hierarchy
#a = '1'
print("The value of a is :" , int(a))

#longint

#tuple
a =1
print("The tuple value of a is " ,tuple('a'))

#set


num = 5+2.0
num_int = int(5.7)
print(num_int)
message = str(42)
print(message)


#ASCII values
char_a ='A'
ascii_a= ord(char_a)
print("The ASCII value of A",ascii_a)

char_b='B'
ascii_b=ord(char_b)
print("The ASCCI value of B is :", ascii_b)

char_c='C'
ascii_c= ord(char_c)
print("The ASCII value of C is :", ascii_c)

char_a ='A'
ascii_a=ord(char_a)
print("The ascii values of ABC is :", ascii_a)

x =65
ascii_x = chr(x)
print("The ascii value of a is :", ascii_x)

#data types
#Interger int () - Whole numbers 12,43.0.-12
#floating point float () - NUmbers having a decimal point
#string str ()  - Ordered sequence of characters ('SIva', "Sankar", "Apple"
#lists List() - unordered sequence of objects whic are kept in []
#dictonories dict()- Unordfered key: value pairs and kept in {"name:Siva", "Age : 28"}
#tulpes tup() - unordered immutable sequences of objects [1,2,43.21,"Siva"]
#sets set() - unordered sets of unique objects {a,b,"}
#booleans () - A logical value indicating true of false