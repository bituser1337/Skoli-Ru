m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

common_divisor = 0

for i in range(1, m+1):
    if n % i == 0 and m % i == 0:
        common_divisor = i

print (common_divisor)
    
