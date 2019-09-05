year = int(input("Input a year: ")) # Do not change this line
year_4 = year // 4
year_100 = year // 100
year_400 = year // 400

if year_4 % 2==1:
    print ("The year is not a leap year")

elif year_4 % 2 == 0:
    year_4 = year_100

elif year_100 % 2 == 1:
    print ("The year is a leap year")

elif year_100 % 2 == 0:
    year_100 = year_400

elif year_400 % 2 == 0:
    print ("The year is a leap year")

elif year_400 % 2 == 1:
    print ("The year is not a leap year")
    
    

    
