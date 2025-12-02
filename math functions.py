import math
from http.cookiejar import http2time

# Circumference of the circle
#radius =  float(input("Input the radius of the circle : " ))
#cmfc = float( 2 * math.pi * radius)
#print(f"The value of the circumference :{round(cmfc, 2) }cm ")

#Area of the circle
#area = math.pi * pow(radius, 2)
#print(f"The area of the circle is : { round(math.pi * pow(radius, 2), 2)}cm²")

a = float(input("Enter the side a : "))
b = float(input("Enter the side b : "))
h = round(math.sqrt(pow(a,2) + pow(b,2)),2)
print(f"The value of the hypotenuse :{h}")

