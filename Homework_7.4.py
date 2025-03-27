def common_elements():
    multiples_of_3 = {x for x in range(1, 301) if x % 3 == 0}
    multiples_of_5 = {x for x in range(1, 501) if x % 5 == 0}
    common = []
    for num in multiples_of_3:
        if num in multiples_of_5:
            common.append(num)
    return common
print(common_elements())