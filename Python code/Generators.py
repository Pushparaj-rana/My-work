
'''1) return

Purpose: Used to return a value from a function and immediately terminate the function's execution.'''


def add(a, b):
    return a + b

result = add(5, 3)  # Returns 8
print(result)  # Output: 8
print()


'''2) YIELD 

Purpose: Used in a generator function to produce a value on-demand without terminating the function's execution.
Behavior: Unlike RETURN, YIELD pauses the function, saving its current state, and allows it to resume later to produce subsequent values.'''

def generate_numbers():
    for i in range(5):
        yield i

for number in generate_numbers():
    print(number)
print()


'''Print Square Sequence using yield'''
def square_num(n):
    for i in range(n):
        yield i*i

for num in square_num(6):
    print(num)