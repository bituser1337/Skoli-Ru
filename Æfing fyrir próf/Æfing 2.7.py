age = int(input("Input age: ")) # Do not change this line

age_float = float(age)
Ticket_cost = 30.0


if age_float >= 65:
    Ticket_cost = Ticket_cost // 2

elif age_float <= 5:
    Ticket_cost = "Free"

else:
    print("Error")


print(Ticket_cost)
