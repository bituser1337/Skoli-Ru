turns = int(input("Enter how many turns: "))

bleh = 0
for i in range(1, turns+1):
    neg_int = int(input("Enter negative ints"))
    if neg_int < 0:
        bleh += 1
        
        

print("The user input negative int", bleh, "Times")
