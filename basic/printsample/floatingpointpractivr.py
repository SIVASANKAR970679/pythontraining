#basic operators

a = 3.5
b = 1.5

print(a+b)
print(a-b)
print(a*b)
print(a/b) #quotient is the answer
print(a//b) # before decimal point is the answer
print(a%b) # remainder is the answer
print(a**b) # power calculation is the answer

#______________________

#roundoff
z =20.52255
print(round(z))
print(round(2.0231))
print(round(3.68))
print(round(z,4))

#--------------------
#COnvert an integer into a float and vice versa
num = 2
print(float(num))
x = 2.9
print(int(x))

#--------------
#Using math calculations
import math

x =16.9
print(math.ceil(x))
print(math.floor(x))
print(math.pi)
print(math.sqrt(x))

#----------------------------------------------
#checking a number is a float or not

def float_num(k):
    return isinstance(k,float)

print(float_num(1.02))
print(float_num(52))


def is_even(n):
    return n%2==0

print(is_even(2))
print(is_even(201))

def x(n):
    return n%2!=0
print(x(5))
print(x(6))

#_----------------------------
#formatiing floats

a = 43.43333
print(f" The four decimal points in a is :{a:.2f}")
print(f"The third decimal point is : {a:.4f}")
print(f"The 10th decimal point is {a:.10f}")

#--------------------------------------------------------
#7. Handling Float Division and Precision Errors

m = 0.1+ 0.2
print(m)
print(round(m,2))

z= 2+6
print(z)

#--------------------------------------------------

#Generating random numbers
import random
print(float(random.uniform(1,4)))

#-----------------------------------------------------
#Summing a list of floats

a =[1.2,3.1]
print(sum(a))
