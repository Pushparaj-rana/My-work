# class Animal:
#     def __init__(self, habitat):
#         self.habitat = habitat

#     def print_habitat(self):
#         print(self.habitat)

#     def sound(self):
#         print("Some Animal Sound")


# class Dog(Animal):
#     def __init__(self):
#         super().__init__("Kennel")

#     def sound(self):
#         print("Woof woof!")


# x = Dog()
# x.print_habitat()
# x.sound()


class teacher:
    def __init__(self):
        None
    
    def print_teacher(self):
        print('i am teacher')

class student(teacher):
    def __init__(self):
        None

    def print_student(self):
        print('i am student')

class youtuber(teacher):
    def __init__(self, name):
        self.name = name

    def  print_youtuber(self):
        print (f'i am youtuber {self.name} ')

x = teacher()
x.print_teacher()
y = student()
y.print_teacher()
y.print_student()
r = "ram"

w = youtuber(r)
w.print_youtuber()
w.print_teacher()



