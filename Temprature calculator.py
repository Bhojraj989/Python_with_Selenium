unit = input("Enter the unit Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature :"))

if unit == "C":
    temp = round((temp *9/5)+32,2)
    print(f"Value in Fahrenheit is {temp}° F")
elif unit == "F":
    temp = round(((temp-32) *5/9),2)
    print(f"Temperature in celsius {temp}° C")
else:
    print("invalid")