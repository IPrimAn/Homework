def is_even(number):
    number = int(number)
    even_nums = ['0', '2', '4', '6', '8']
    for i in range(5):
        if str(number)[-1] == even_nums[i - 1]:
            return True
        if i == 4:
            return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')