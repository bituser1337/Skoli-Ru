a = int(input("Enter integer a"))
b = int(input("Enter integer b"))
choice = int(input("Enter choice"))

the_sum = 0

if choice == 1:
    the_sum = a + b

elif choice == 2:
    the_sum = b - a

elif choice == 3:
    the_sum = a * b

else:
    print("invalid input")

if choice <= 3:
    print(the_sum)
