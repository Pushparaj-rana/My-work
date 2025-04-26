from collections import deque
stack = deque()

class XX:
    def __init__(self):
        self.container = deque()
    def push (self,val):
        self.container.append(val)
    def pop (self):
        self.container.pop()
    def peek (self):
        self.container[-1]
    def size (self):
        return len(self.container)
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            False
    def __str__(self):
        return str(self.container)

s = XX()           
s.push(8)
s.push(6)
s.push(22)
print(s)
s.pop()
print(s)
