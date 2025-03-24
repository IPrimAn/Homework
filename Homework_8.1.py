def add_one(some_list):
    num = ""
    for digit in some_list:
        num += str(digit)
    number = int(num) + 1
    result = []
    for digit in str(number):
        result.append(int(digit))
    return result
print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([3, 5, 6, 6, 7, 3, 8]))
###
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'test2'
assert add_one([3, 5, 6, 6, 7, 3, 8]) == [3, 5, 6, 6, 7, 3, 9], 'test3'