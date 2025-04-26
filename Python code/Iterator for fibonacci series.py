class fibonacci:
    def __init__(self,limit):
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration
        

# init the fib_iterator
fib_iterator = fibonacci(6)
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break