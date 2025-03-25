num = int(input('enter number: '))
error_check = 0
while num > 9:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product
    error_check += 1
    if error_check > 10:
        print('error, repeated too many times')
        break
if error_check <= 10:
    print(num)
