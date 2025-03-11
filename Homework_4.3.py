import random
from re import search

my_list = [random.randint(1, 9) for i in range(random.randint(3, 10))]
print(my_list)
new_list = my_list[0:3:2]
new_list2 = [my_list[-2]]
new_list.extend(new_list2)

print(new_list)