num_int = int(input("Enter the number you want to find the square root of"))
guess_float = float(input("Guess the square root of the number"))
tolarence_float = float(input("What is your tolarance"))
# 3 inputs, two int's and one float


orignal_guess_int = guess_float
count_int = 0
previous_float = 0

while(previous_float - guess_float) > tolarence_float:
    previous_float = guess_float
    quotient_float = number_int/guess_float
    guess_float = (quotient_float + guess_float)/2
    count_int = count_int + 1

#Do the algorithm




#output the three original values, the number of




#iterations and the square root

print("Square root of", num_int, " is", guess_float)
print("Took ", count_int, "reps to get it to tolerance: ", tolarence_float)
print("Starting from a guess of: ", original_guess_int)
