import keyword
import string
your_variable = input('write name for variable and we will check it: ')
print(your_variable.islower())
print(not your_variable[0].isdigit())
print(not your_variable == keyword.kwlist)
print(your_variable == string.punctuation)
print(not your_variable >= '_'*2)
