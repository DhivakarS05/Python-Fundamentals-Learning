foods = []
prices = []
total = 0

while True:
    food = input("Order a Food or (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter amount of the {food}: "))
        foods.append(food)
        prices.append(price)

print("-----ordered food-----")
for i in foods:
    print(i, end=" ")
print()

for j in prices:
    total +=j
print(f"Total amount of your ordered food is {total} rupees")
if total > 40.00:
    total -=2
    print(f"Discount % amount is 2 rupees")
print(f"Total amount you have to pay is {total} rupees")
print("Thankyou for ordering food")


