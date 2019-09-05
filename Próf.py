age = int(input("Enter your age: ")) #User inputs age

if age > 0 and age < 35: #If the input is between 0 and 35 the program prins "Young"
    print("Young")

if age >= 35 and age <=50: #If the input is between 35 and/or equal to 50 the program prints out "Mature"
    print("Mature")

if age > 50 and age < 70: #If the input is between 50 and 70 the program prints out "Middle-aged"
    print("Middle-aged")

if age >= 70: #If the input is more than 70 the program prints out "Old"
    print("Old")

if age < 0: #If the age is below zero the program prints out "Invalid age"
    print("Invalid age")
