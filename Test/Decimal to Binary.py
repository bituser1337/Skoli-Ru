decimal = int(input("enter decimal"))

binary = 1
remainder = 0



while decimal > binary:
    if decimal % 2 == 1:
        binary = 1
        binary = binary * 1
    if decimal % 2 == 0:
        binary = 0
        binary = binary * 0
    decimal = decimal // 2
    print (binary)


#Step1: Enter the decimal number.
#Step2: Using while loop
   #*Divide the number it by 2. Find both remainder and quotient.
#Take another variable initialized with 1. 
   #Now remainder will be multiplied with this variable and added with the final output number.
    #That variable will be incremented by 1.
   #*The first remainder is the last digit in the sequence.
#Step3: Display the value.
