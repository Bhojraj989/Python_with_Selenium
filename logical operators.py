# temp= 25
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is scheduled as planned")
from calendar import day_abbr

is_pwr = False
is_r1_tv = True
is_r1 = True

if is_pwr and is_r1 and is_r1_tv :
    print("What do you want to see? ")
elif  is_pwr and is_r1 and  not is_r1_tv:
    print("TV is ON but not connected to internet")
elif is_pwr and not is_r1 and is_r1_tv:
    print("TV connected to router but no internet")
elif not is_pwr and is_r1 and is_r1_tv:
    print("No electricity")