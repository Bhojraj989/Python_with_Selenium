# while loop : this will run till the condition stays true


name = input("Enter your name : ")

while name == "":
    print('''You did not enter your name.''')
    name = input("Enter your name : ")
print(f"Hi {name}!!!")