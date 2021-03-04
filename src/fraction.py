class fraction:
    def __init__(self, t, b):
        self.top = t
        self.bottom = b

    def __mul__(self, other):
        return fraction(self.top * other.top, self.bottom * other.bottom)

    def __truediv__(self, other):
        return fraction(self.top * other.bottom, self.bottom * other.top)

    def __sub__(self, other):
        return fraction(self.top * other.bottom - other.top * self.bottom, self.bottom * other.bottom)

    def __add__(self, other):
        return fraction(self.top * other.bottom + other.top * self.bottom, self.bottom * other.bottom)

    def __gt__(self, other):
        if (self.top / self.bottom > other.top / other.bottom):
            return True
        return False

    def __str__(self):
        return str(self.top) + " / " + str(self.bottom)

x = fraction(1,2)
y = fraction(1,3)
sum = x + y
print(f'Sum is {sum}')

mull = x * y
print(f'Product is {mull}')

div = y / x
print(f'Quotient is {div}')

sub = x - y
print(f'Difference is {sub}')

z = x + y
print(f'Z = {z}')   # __str__

if (x > y):
    print("x is greater than y")
elif (y > x):
    print("y is greater than x")
else:
    print('Objects are equal')