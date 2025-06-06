import math

x = 9.8

print(math.ceil(x))   # Rounds up (10)
print(math.floor(x))  # Rounds down (9)
print(math.sqrt(x))   # Square root
print(math.pi)        # Pi value

#pop a element
set12 = { 1,2,3,4,56,76}
set12.pop()
print(set12)

#Basic Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

def wish(name:str):
    return f"Hello, \t {name}"
print(wish("Siva"))


#Multiple Parameters
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 10))  # Output: 15
def add(a,b):
    return a+b
print(add(6,6))


def addition (a:int,b:int)->int:
    return a+b
print(add(43.3,32.2))



sandeep_team = ["siva","bharath","srinu","naresh","rahul","laxmi","lokesh","venu"]
siva_team = ["manoj","sateesh","sreekanth","D naresh","ramana","sivamanju","karthik","narendra","guna","sai"]
rohin_team = ["Satish","nithya","mahesh","delli","vijay","pradeep","B karthik","Rajesh","Kishore"]

tirupati_team = sandeep_team+rohin_team+siva_team
print(tirupati_team)
FTC_name = input("Enter the FTC name :")


if FTC_name in sandeep_team:
    print(f"{FTC_name} is belongs to sandeep")
elif FTC_name in siva_team:
    print(f"{FTC_name} is belongs to Siva team")
elif FTC_name in rohin_team:
    print(f"{FTC_name} is belongs to Rohin team")
else:
    print("Entered name is not in anyone's team. Kindly check and try again")
