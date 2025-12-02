# Dictionary : It is the pair of two things key and a value associated with it. No DUPLICATES.
from selenium.webdriver.common.devtools.v135.page import print_to_pdf

capitals = {"India": "New Delhi",
            "USA": "Washington DC",
            "Japan":"Tokyo",
            "Russia":"Moscow"}

# print(capitals)
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Japan") :
#    print("That capital exists.")
#else:
#    print("That capital doesn't exists.")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Pakistan"})

# capitals.pop("USA")
# capitals.popitem()
# print(capitals)

# keys = capitals.keys()
# #print(keys)
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# # print(values)
# for value in capitals.values():
#     print(value)

items = capitals.items()
# print(items)
for keys, values in capitals.items():
    print(f"{keys}: " "{values}")
