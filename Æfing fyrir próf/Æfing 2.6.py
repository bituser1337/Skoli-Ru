d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

the_sum = d1 + d2

if d1 < 1 and d1 > 6:
    print ("Invalid input")
elif d2 < 1 and d2 > 6:
    print ("Invalid input")

elif the_sum == 7 :
    print ("Winner")

elif the_sum == 11 :
    print ("Winner")

elif the_sum == 2:
    print ("Loser")
    
elif the_sum == 3:
    print ("Loser")
    
elif the_sum == 12:
    print ("Loser")

else:
    print (the_sum)
    
