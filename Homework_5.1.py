import keyword
import string
your_variable = input('write name for variable and we will check it: ')
for i in range(1):
    symbols = string.punctuation
    symbols2 = symbols.replace('_', '')
    count_symbol = your_variable.count("_")
    check = 0
    r1 = your_variable.islower()
    r2 = not your_variable[0].isdigit()
    r3 = not your_variable == keyword.kwlist
    r4 = not your_variable.index(your_variable) == symbols2
    r5 = not count_symbol >= 2
    if r1 and r2 and r3 and r4 and r5 == True:
        print(True)
    else:
        print(False)