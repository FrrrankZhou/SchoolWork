class MyMatrix:
    def __init__(self, a):
        if type(a) != list and type(a) != tuple:
            raise TypeError("Please enter the matrix as a 2d list")
        self.matrix = tuple(tuple(row) for row in a)

    def __add__(self, b):
        if type(b) != MyMatrix:
            raise TypeError("Please add two vectors together")
        elif len(b[0]) != len(self[0]) or len(self) != len(b):
            raise ValueError("Only matrices with same size can be added together")
        return MyMatrix([[self[i][j] + b[i][j] for i in range(len(self))] for j in range(len(self[0]))])

    def __sub__(self, b): return self + -1*b

    def __mul__(self, b):
        if type(b) == int or type(b) == float:
            return MyMatrix([[self[i][j] * b for i in range(len(self))] for j in range(len(self[0]))])
        elif type(b) == MyMatrix:
            if len(self[0]) != len(b):
                raise ValueError("The width of the former should be equal to the height of the latter")
            return MyMatrix([[sum(self[i][n] * b[n][j]for n in range(len(self[0])))
                              for j in range(len(b[0]))]
                             for i in range(len(self))])
        else:
            raise TypeError("Only a number or a matrix can times a matrix")

    def __repr__(self):
        x, y = len(self), len(self[0])
        space = max([len(str(self[i][j]))for i in range(x)for j in range(y)])
        return "\n".join([("".join([str(self[i][j]).ljust(space+1)for j in range(y)]))for i in range(x)])

    def __getitem__(self, i):
        if isinstance(i, int):
            return self.matrix[i]
        elif isinstance(i, slice):
            return MyMatrix(self.matrix[i])
        elif isinstance(i, tuple):
            if type(i[0]) != slice and type(i[1]) != slice:
                raise TypeError("This is a matrix, not tensor")
            return MyMatrix(tuple(row[i[0]] for row in self[i[1]]))

    def __len__(self): return len(self.matrix)


def __decide(i, j): return 1 if i == j else 0


def unit_matrix(size): return MyMatrix([[__decide(i, j) for j in range(size)]for i in range(size)])


def entering(m, n):
    return MyMatrix([[float(input("The element at (%s, %s) is: " % (i, j)))for j in range(n)] for i in range(m)])
