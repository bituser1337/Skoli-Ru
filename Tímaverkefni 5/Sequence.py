n = int(input("Enter the length of the sequence: ")) # Do not change this line

the_sum = 0
int_1 = 1
int_2 = 2
int_3 = 3


if n > 0:
    print(int_1)
if n > 1 :
    print(int_2)
if n >2 :
    print(int_3)

if n > 3:
    for i in range(n-3):
            the_sum = int_1 + int_2 + int_3
            print(the_sum)
            int_1 = int_2
            int_2 = int_3
            int_3 = the_sum


    
