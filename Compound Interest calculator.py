principle = 0
rate = 0
time = 0

while principle <= 0:
    principle= float(input("Enter the value of principle : "))
    if principle <= 0:
        print("Principle can't be negative or Zero.")


while rate <= 0:
    rate = int(input("Enter the value of rate : "))
    if rate <= 0:
        print("rate can't be negative or Zero.")

while time <= 0:
    time = int(input("Enter the value of time in years: "))
    if time <= 0:
        print("time can't be negative or Zero.")

total = principle * pow((1+ rate/100),time)
print(f"Your total amount is : ${round(total,2)}")