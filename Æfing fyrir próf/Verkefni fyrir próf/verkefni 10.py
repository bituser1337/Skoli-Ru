num = int(input("enter int: "))

if num < 10 and num > 0:
    print("Less than 10: ")

elif num >= 10 and num < 20:
    print("Between 10 and 20")

elif num >= 20:
    print("The value is too high!")

else:
    print("the value is too low!")
