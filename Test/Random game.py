import random
number = random.randint(0,100)

print ("Hi Lo game please enter a number between 0 and 100. ")
print()

guess_str = input("Guess a number: ")
guess = int(guess_str)

while 0 <= guess <= 100:
    if guess > number:
        print("guessed too high.")
    elif guess < number:
        print("guessed too low.")
    else:
        ("YAYYY you guessed it the number was", number)
        break

        guess_str = input("Guess a number:")
        guess = int(guess_str)
else:
    print("you quit early, the number was:", number)

