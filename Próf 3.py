first = int(input("First: ")) #The user inputs integer
step = int(input("Step: "))

ultra_sum = first #variable that will be used so that the sum won't go over 100

print (first, end=' ') #print the "first" input
for i in range(first, 100+1): #The loop keeps going until it goes to 100"
    first = first + step #counter that sums up first and step
    print(first, end=' ') #prints out the value of first += step
    ultra_sum += first #This sums up all the numbers 
    if ultra_sum >= 100: #If the number value goes higher than 100 the loop breaks
        break
    

print("Sum of series:", ultra_sum ) #prints out the sum of all input values
    
                 
