#print formatting with placeholders
print("Hi,My name is %s" %'siva')
print("My age is %d"%28)
print("I want to learn %s programming language in %.1f months" %('python',1.5))
print("Daily I'm going to %r on my bike" %'office')
print("At the time cold we have to maintain some %s" %'space \t with others')

#padding and precision of floating numbers
a = 2.43
c = 3232.542
b = 234.87988
print('The floating value of %.2f' %a)
print("The 2 values of a decimal number b is %.f" %b)
print("The value a floating number is %.10f" %c)
print("The value of c is {}".format(c))

#formatting by using format() menthod
#method 1
print("{} is working in {} from last {} months" .format('Siva', 'Bajajfinance',8.710))

#method 2
a = 'apple'
b = 'banana'
c = 'orange'
print("An {0} is in %s color. A {1} is in yellow color. An {2} is in light orange color" .format(a,b,c))

#method2
name = 'Siva'
print(f"{name} is very aggressive guy. {name} is trying to learn python programming language.")
#methid 3
a , b ,c ,d = 'siva', 'chandana', 'Dharshi','Yeeyansh'
print(f"My name is {a} and my wife name is {b}. I have to kids. Elder one is {c} and younger son is {d}")
#method 4
print("In my company one funda is there which is Do {a} and earn {a}" .format(a='more'))
