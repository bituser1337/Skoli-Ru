top_num = int(input("Upper number for the range: ")) # Do not change this line
import math

n=1

for n in range(1, top_num):
    if n == 3 or n == 5:
        continue
    perfect_number= 2**n*((2**(n+1)-1))#formula
    if perfect_number > top_num:
        break    
    
    print(perfect_number)

