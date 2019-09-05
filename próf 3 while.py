first = int(input("First"))
step = int(input("Step"))

ultra_sum = 0

while ultra_sum < 100:
    first+= step
    print(first)
    if ultra_sum > 100:
        break
    ultra_sum += first
    
    print(ultra_sum)
