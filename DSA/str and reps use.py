class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, aged {self.age}'

    def __repr__(self):
        return f'Person(name="{self.name}", age={self.age})'

# Creating an instance of Person
person = Person("Alice", 30)

# Using print (calls __str__)
print(person)  # Output: Alice, aged 30

# Using repr (calls __repr__)
print(repr(person))  # Output: Person(name="Alice", age=30)
