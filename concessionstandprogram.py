menu = {"popcorn":60 ,
        "pepsi":40,
        "coffee":30,
        "puffs":25,
        "pizza":80,
        "burger":70,
        "sweetcorn":35}
cart = []
total = 0
print("------- Menu -------")
for key,value in menu.items():
    print(f"{key:10}Rs:{value}")

while True:
    food = input("Enter your food(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------- you ordered ---------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"your total amount of ordered food is : Rs.{total}")
print("------- Thankyou -------")