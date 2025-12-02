# list [] - ordered and changeable, duplicates OK
# set {}  - unordered and immutable, add/remove OK, NO duplicates
# tuple ()- ordered and unchangeable, duplicates OK, FASTER
from traceback import print_tb

fruits = [ "banana","Apple", "orange", "coconut", "Apple"]

# print(fruits) # print list
# print(fruits[0])  # print index 0 only. ( Index started from 0 ).

fruits.append("pizza")
# fruits.insert(0,"mango")
# fruits.sort(MMMango")
#loops to print list using for loop.

# fruits.remove("Apple")
for fruit in fruits:
    print(fruit)

# print(fruits[::-1])  # print reversed order

print(fruits.count("Apple"))


