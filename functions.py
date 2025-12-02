#
# def happy_birthday():
#     print("Happy birthday to you! ")
#     print("You are years old !")
#     print()
#
#
# happy_birthday()
# happy_birthday()
#
# def menu_rate(rate, quntity):
#     print(f"Tomato - ${rate} per {quntity}Kg")
#
# menu_rate(40,2)
#
# def car(brand, year, price):
#     print(f"This car is {brand} made in {year}")
#     print(f"The price of {brand} is ${price}")
#
# car("Bugati", 1989, 100000)

# def create_name ():
#     First_name = input("Enter you name : ")
#     Last_name = input("Enter your last : ")
#     First_name.capitalize()
#     print(f"{First_name.capitalize()} {Last_name.capitalize()}")
#
# create_name()

def create_name(x, y):
    first = x.capitalize()
    last = y.capitalize()
    name = first + " " + last
    return name

print(create_name("john", "wick"))

def create_name1(name,title,age):
    print(f"{name} {title} {age}")

create_name1(name="Bro" ,title="Mr", age=55)