"""
 Python program to check if the number is an Armstrong number with \
 the index of 3 or not
 for input try numbers 153, 370, 371, 407
"""
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
SUM1 = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    SUM1 += digit ** 3
    temp //= 10

# display the result
if num == SUM1:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
