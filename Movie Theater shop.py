import time

menu = {"soda": 3.00,
        "pizza": 5.00,
        "samosa": 5.00,
        "burger": 6.00}
cart =[]
total = 0
print("------- Menu --------")
for item, value in menu.items():
    print(f"{item:10}: ${value:.2f}")
print("---------------------")

print()
while True:
    food = input("Enter the food you want : ").lower()
    if food == "q":
            break
    elif menu.get(food) is not None:
        cart.append(food)

print()
print("----- Your Cart -----")
for food in cart:
    total = total + menu.get(food)
    print(f"{food}", end=" ")

print()
print(f"Your total is ${total}")
print("---------------------")

