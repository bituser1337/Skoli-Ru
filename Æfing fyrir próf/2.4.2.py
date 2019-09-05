year = int(input("enter a year"))

if year / 4 == year // 4:

    if year / 100 == year // 100:

        if year / 400 == year // 400:
            leap_year = True


        else:
            leap_year = False

    else:
        leap_year = True
    

else:
    leap_year = False


print (leap_year)    
