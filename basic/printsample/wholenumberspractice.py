#addition
#from time import process_time
from time import process_time

a = 29
b = 2
print("the value of a and b is ", a+b)
print("The value of a - b is ", a-b)
print("The value of a*b is ", a*b)
print("The division value of a/b is ",a/b) # the value of a/b is quotient
print("The floor division value of a//b is ", a//b) # floor division of  a//b is first value of means "The value of digits in Quotient
print("The modulo of a%b is ", a%b)  # Module of a%b is "The remainder of a and b
print("The power of a**b is ", a**b) #The ** indicates power calculations "a power b"

#Using BODMAS rule
print("The value of (a+b)*(a-b) is ",(a+b)*(a-b))
c = (a+b)*(a-b)
print("The value of ",c)

print(a+b+c)
a = a+a
print(a)

print(a+b)

my_salary = 53000
my_emi = 32000
print( "the balance of my salary is " ,my_salary-my_emi)
print("The product of my salary is ", my_salary * my_emi)
#_________________________________________________________________________________________________________

a = 25
b = 3
c = a+b
print("The sum of a+b is ",a+b) #addition
print("The value of  a-b is ", a-b) #substraction
print("The value of a*b is ", a*b)  #Multiplicaton or product of two values
print("The value of a/b is ", a/b) # Division of a/b and we will get quotient is the answer
print("The value of a//b is ", a//b) # a//b means floor value of the a//b which means value before decimal point
print("The value of a%b is" , a%b) # % represents the modulo  and remainder will be the answer
print("The value of a**b is ", a**b) #** means the power .
print("the vale of %s ", (a+b)%(a-b)) #BODMAS
print(a+b*c*a/b) #BODMAS

a=a+a
print(a)
my_salary = 53000
my_emis =35000
petrol = 2
print("Balance salary is " , my_salary-my_emis)
print("petrol expenses is " ,my_salary//petrol)