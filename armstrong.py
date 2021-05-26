"""
 Python program to check if the number is an Armstrong number with \
 the index of 3 or not
 for input try numbers 153, 370, 371, 407
"""
def armstrong_check(num):
    SUM1 = 0
    print(num)
    temp = num
    while temp > 0:
        digit = temp % 10
        SUM1 += digit ** 3
        temp //= 10

    if num == SUM1:
        return True
    else:
        return False