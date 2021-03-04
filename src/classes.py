class Dog:
    # Class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def print(self):
        print(self.name, self.age)

x = Dog("Rex", 2)
y = Dog("Jack", 3)

#print(x.name, x.age)
#print(y.name, y.age)

x.print()
y.print()

a = 5
b = 6

#print(a)