import math


class MyVector:
    def __init__(self, a):
        if tuple != type(a) and list != type(a):
            raise TypeError("Please enter the vector as a list or tuple")
        self.vector = tuple(a)

    def __add__(self, b):
        if type(b) != MyVector:
            raise TypeError("Please add two vectors together")
        elif len(b) != len(self):
            raise ValueError("Only vectors with same dimension can be added together")
        return MyVector([(self[i] + b[i]) for i in range(len(self))])

    def __abs__(self): return sum(self[i] ** 2 for i in range(len(self))) ** 0.5

    def __sub__(self, b): return self+-1*b

    def __mul__(self, b): return MyVector([c * b for c in self.vector])

    def __rmul__(self, b): return self * b

    def __truediv__(self, b): return MyVector([(c / b) for c in self.vector])

    def dot_product(self, b):
        if type(b) != MyVector:
            raise TypeError("Please multiply two vectors together")
        elif len(b) != len(self):
            raise ValueError("Only vectors with same dimension can be multiplied together")
        return sum(self[i] * b[i] for i in range(len(self)))

    def cross_product(self, b):
        if type(b) != MyVector:
            raise TypeError("Please multiply two vectors together")
        elif len(b) != 3 or len(self) != 3:
            raise ValueError("Please multiply two three-dimensional vectors")
        return MyVector([self[1]*b[2] - self[2]*b[1], self[2]*b[0] - self[0]*b[2], self[0]*b[1] - self[1]*b[0]])

    def angle(self, b, mode="radian"):
        if type(b) != MyVector:
            raise TypeError("Please multiply two vectors together")
        elif len(b) != len(self):
            raise ValueError("Only vectors with same dimension can be multiplied together")
        if mode == "radian":
            return math.acos(self.dot_product(b) / (abs(self) * abs(b)))
        elif mode == "degree":
            return math.acos(self.dot_product(b) / (abs(self) * abs(b)))*180/math.pi

    def __repr__(self): return "\n".join([str(self[i]) for i in range(len(self))])

    def __len__(self): return len(self.vector)

    def __getitem__(self, i): return MyVector(self.vector[i]) if isinstance(i, slice) else self.vector[i]
