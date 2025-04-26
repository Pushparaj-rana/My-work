# def factorial_it(func):
#     def wrap(*args,**kwargs):
#         if int(*args,**kwargs) < 0:
#             return "Negative integer"
#         elif type(*args,**kwargs) != int:
#             return 'not integer'
#         else:
#             fac = func(*args,**kwargs)
#             return fac
#     return wrap

# @factorial_it
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(1))




# SAME CODE- CODE BY CHAT-GPT

import functools

def factorial_it(func):
    @functools.wraps(func)  # Preserves function metadata
    def wrap(*args, **kwargs):
        if len(args) != 1 or not isinstance(args[0], int): # Ensure only one argument pass and it's integer. use args[0] for first possition argument
            return "Not an integer"
        if args[0] < 0:
            return "Negative integer"
        else:
            return func(*args, **kwargs)  # Call the original function
    return wrap

@factorial_it
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(4))  # Output: 24
print(factorial(-3))  # Output: Negative integer
print(factorial(3.5))  # Output: Not an integer




#Decorator coding by Mr.patel

def check(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


@check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    e.print_exception()

try:
    print(factorial(1.354))
except Exception as e:
    e.print_exception()