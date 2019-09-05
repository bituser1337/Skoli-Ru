the_sum = 0 #Breyta sem verður notuð til þess að summu talnanna
odd_number = 0 #Breyta sem verður notað til þess að finna oddatölur
even_number = 0 #Breyta sem verður notað til þess að finna sléttar tölur
largest_int = 0 #Breyta sem verður notað til þess að finna stærstu töluna
Cumlative_total = 0 #Breyta sem verður notað til þess að finna summu talnanna
firstPass = True #Gert til þess að fá annað input ef að fyrsta talan verður 0

while True: # Lykkjan keyrir þar til að "break condition finnist"
    number_int = int(input("Enter an integer: ")) #Beðið um input frá notandanum
    if number_int % 2 == 1: #Ef að remainder af tölunni verður einn þá er hún oddatala
        odd_number += 1 #Counter sem segir til hversu margar oddatölur hafa verið slegnar inn
    if number_int % 2 == 0:# Ef remainder verður 0 þá er talan slétt tala
        if number_int != 0:
            even_number += 1 #Counter sem segir hversu margar sléttar tölur hafa verið sleganr inn
    if number_int > largest_int: #Ef að talan seam sleginn er stærst þá breytist breytan yfir í "largest int"
        largest_int = number_int

    if number_int == 0 and firstPass == False: # Ef að talan er 0 og lykkjan hefur ekki farið einu sinni í gegn þá "breaker" loopan
        break

    if number_int != 0: # Ef talan er ekki núll þá heldur lykkjan áfram
        the_sum += number_int #Counter sem plúsar alltaf input
        Cumlative_total +=  number_int        
        print ("Cumulative total: ", Cumlative_total) #Prentar út summuna í hvert sinn sem loopan fer i gegn
        firstPass = False #Ef talan er ekki 0 þá verður firstpass = false
    
    

if the_sum != 0: # Ef summan er ekki 0 þá prentast þessar breytur
    print ("Largest number",(largest_int))
    print ("Count of even numbers", even_number)
    print ("Count of odd numbers", odd_number)

