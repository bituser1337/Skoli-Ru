n = int(input("Input a natural number: ")) # Do not change this line
toggle = 0
prime = 2
factors = []
tester = 1
# Fill in the missing code below
while n >= tester:
    if (n % tester == 0):
        factors.append (tester)
    tester += 1
prime = False
if len(factors)==2:
    prime = True
if prime:
    print("Prime")
else:
    print("Not prime")
