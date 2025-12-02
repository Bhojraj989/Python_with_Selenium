foods = []
prices = []
total = 0

while True:
    food = input("Enter name of the food ( q to quit ) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} : $ "))
        foods.append(food)
        prices.append(price)

print("-------Your Cart--------")
for food in foods:
    print(food,  end=" ")

for price in prices:
    total += price
print()
print(f"Your total sum is : {total}")



