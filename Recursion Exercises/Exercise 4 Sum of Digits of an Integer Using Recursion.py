import math

def sum_digit(num):
    sum = 0
    if num > 0:
        
        r = num%10
        i = num/10
        I = math.floor(i)
        sum = r + sum_digit(I)
    return sum



print(sum_digit(144))
print(sum_digit(16))


