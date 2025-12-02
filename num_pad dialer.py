# Create a num pad dialer for the phone and the should be matched with a phone keypad without any braces or brackets.
# Here we can use list and tuples but as we dont need to change the output again and again we can use tuples as these are faster than list.


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for number in num_pad:
    for nos in number:
        print(nos, end = " ")
    print()