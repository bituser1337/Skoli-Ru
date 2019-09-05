turns= int(input("Enter turns: "))

int_sum = 0
for i in range(1, turns+1):
    int_input = int(input("Enter integer: "))
    if int_input < 0:
        int_sum += int_input

print(int_sum)
