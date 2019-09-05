turns = int(input("Enter how many turns: "))

blehh = 0
bleh = 0

for i in range(1, turns+1):
    input_int = int(input("Enter how many int: "))
    if input_int < 0:
        blehh += 1
    if input_int > 0:
        bleh += 1

print ("The user entered postive int", bleh, "Times", "and negative int", blehh, "times")
