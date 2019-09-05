top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1, top_num):
    perfect_number= 2**i*((2**(i+1)-1))#formula
    if perfect_number > top_num:
        break
    print(perfect_number)
