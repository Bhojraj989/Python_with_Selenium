# Print string
from operator import truediv
from selectors import SelectSelector

print("I like pizza")
print("I also like cars")

# Print interger
print(12346)
num_missed = 5
print(f"Above string does not have {num_missed} ")

#print floating point numbers
print(23.55)
item_price = 35.99
print(f"this is the price of 1 article {item_price}")

#boolean
is_online = False
is_passed = True
print(f"You are connected to internet : {is_online}")
print(f"You have passed your exam : {is_passed}")
if (is_passed):
    print("You have passed the exam")
else:
    print("You have to come again to study")

if(is_online):
    print("Hi there! You are online now ")
else:
    print("Sorry you are not connected to internet")