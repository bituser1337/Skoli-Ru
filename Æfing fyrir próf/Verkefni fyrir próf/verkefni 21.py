turns = int(input("Enter turns"))
print ("You picked", turns, "turns")

int_value = int(input("Enter integer value"))
print ("you picked", int_value)

for i in range(1, turns):
    if int_value % 2 == 1:
        int_value= int(input("Enter integer value"))
        print ("you picked", int_value)
