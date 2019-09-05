num1 = int(input("Enter the first int: " ))
num2 = int(input("Enter the second int: "))
num3 = int(input("Enter the third int: "))

if num1 < num2 and num1 < num3:
    print("Num1 is the lowest")

if num2 < num1 and num2 < num3:
    print("Num 2 is the lowest")

if num3 < num1 and num3 < num2:
    print("Num 3 is the lowest")
