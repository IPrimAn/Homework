import keyword
import string
symbols = string.punctuation
symbols2 = symbols.replace('_', '')
your_variable = input('write name for variable and we will check it: ')
for i in range(5):
    r1 = your_variable.islower()
    r2 = not your_variable[0].isdigit()
    r3 = not your_variable == keyword.kwlist
    r4 = your_variable == symbols2
    r5 = not your_variable >= '_'*2
    if r1 == False:
        print(False)
        break
    if r2 == False:
        print(False)
        break
    if r3 == False:
        print(False)
        break
    if r4 == False:
        print(False)
        break
    if r5 == False:
        print(False)
        break
    else:
        print(True)