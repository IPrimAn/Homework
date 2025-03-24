def find_unique_value(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num
numbers = [1, 2, 1, 1, 3, 7, 0, 0, 2, 9, 3, 7]
special = find_unique_value(numbers)
assert find_unique_value([1, 2, 1, 1, 3, 7, 0, 0, 2, 9, 3, 7]) == 9, 'test1'
print(f'your special number is: {special}')
