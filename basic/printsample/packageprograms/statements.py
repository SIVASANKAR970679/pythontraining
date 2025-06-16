from time import process_time

num = int(input("Enter a number :"))

if num>=1:
    print(f"The entered number {num} is a positive number")
elif num<=-1:
    print(f"The entered number {num} is a negative number")
else:
    print("Entered number is 0")

#5. Calculate Electricity Bill Based on Units

units = int(input("Enter the electricity units : "))

if units < 100:
    bill = units*5
elif units<300 and units>=100:
    bill = units*7
else:
    bill = units*10

print(f"The electricity bill is : {bill}")

#3. Determine Triangle Type Based on Sides
side_A = int(input("Enter the length of side A :"))
side_B = int(input("Enter the length of side B :"))
side_C = int(input("Enter the length of side C :"))

if side_A==side_B==side_C:
    print("ALl sides are equal so it is an ENQUILENT TRIANGLE")
elif side_A==side_B or side_B==side_C or side_C==side_A:
    print("Two sides are equal so it is Isol")