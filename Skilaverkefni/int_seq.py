number_int = int(input("Enter an integer: ")) #Forritið biður notandan um input

the_sum = 0 #Breyta sem verður notið til þess að summa tölur
odd_number = 0 #Breyta sem verður notuð til þess að finna oddatölur
even_number = 0 #Breyta sem verður notuð til þess að finna sléttar tölur
largest_int = 0 #Breyta sem verður notið til þess að finna stærstu töluna

cumlative_total = the_sum + number_int #Breyta sem verður notuð til að summa tölur

while number_int > 0: #Lykkjan heldur áfram svo lengi sem að talan er stærri en 0
    if number_int % 2 == 1: #Ef remainder af inputi er 1 þá er talan oddatala
        odd_number += 1 #Counter sem er notaður til þess að telja allar oddatölur
    if number_int % 2 == 0: #Ef remainder af inputi er 0 þá er talan slétt tala
        even_number += 1 #Counter sem er notaður til þses að telja allara sléttar tölur
    if number_int > largest_int: #Ef inputið er hærra en stærsta talan þá breytist þá verður stærsta talan "largest_int" að inputin eða "number_int"
        largest_int = number_int
    print ("Cumulative total:", cumlative_total) #Prentar út summuna á hverri tölu fyrir sig
    number_int = int(input("Enter an integer: ")) #Biður notandan um input svo lengi sem að talan er ekki 0
    the_sum += number_int #Þetta er counter sem að bætir alltaf inputinu við sjálfan sig
    cumlative_total +=  number_int #Þetta er counter sem bætir inputinu við cumlative_total


if cumlative_total != 0: # ef að summan er ekki 0 þá prentast "largest_int" "even_number" og "odd_number"
    print ("Largest number:",(largest_int))
    print ("Count of even numbers:", even_number)
    print ("Count of odd numbers:", odd_number)


     
