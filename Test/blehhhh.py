print ("allow the user to enter a series of integers. Sum them.")

number_int = int(input("number: "))

the_sum = 0
odd_number = 0
even_number = 0
largest_int = 0

Cumlative_total = the_sum + number_int

while number_int != 0:
    if number_int < 0:
        number_int = int(input("number: "))
        break
    if number_int % 2 == 1:
        odd_number += 1
    if number_int % 2 == 0:
        even_number += 1
    if number_int > largest_int:
        largest_int = number_int
    print ("Cumulative total :", Cumlative_total)
    number_int = int(input("Number: "))
    the_sum += number_int
    Cumlative_total +=  number_int
    continue
    
    
print ("Largest number",(largest_int))
print ("Count of even numbers", even_number)
print ("Count of odd numbers", odd_number)

     

