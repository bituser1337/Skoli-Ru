par = int(input("Enter the par of the hole 1: "))
score = int(input("Enter your score of hole 1: "))

counter = 0
input_counter = 1
while counter <17:
    counter += 1
    input_counter +=1
    if score == par - 3:
        print("albatross")
    if score == par -2:
        print("eagle")
    if score == par -1:
        print("birdie")
    if score == par:
        print("par")
    if score == par +1:
        print ("bogey")
    if score == par +2:
        print ("douple bogey")
    if score == par +3:
        print ("triple bogey")
    if score > par +4:
        print ("bad hole")
    par = int(input("Enter the par of the hole {}: ". format(input_counter)))
    score = int(input("Enter your score of hole {}: ". format(input_counter)))
    continue
    
    
   
        

    
