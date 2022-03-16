class Polynomial:
    def __init__(self, vector): self.polynomial = vector

    def __len__(self): return len(self.polynomial)

    def __getitem__(self, i): return self.polynomial[i]

    def __call__(self, x): return sum(self[i] * x ** i for i in range(len(self)))

    def __repr__(self):
        out = str(self[0])if self[0] != 0 else""
        if self[1] > 0:
            out = out+" + %sX" % self[1]
        elif self[1] < 0:
            out = out+" - %sX" % -self[1]
        for i in range(2, len(self)):
            if self[i] < 0:
                sign = " - "
            elif self[i] > 0:
                sign = " + "
            else:
                sign = ""
            if abs(self[i]) == 1:
                out = "%s%sX%s" % (out, sign, i)
            elif self[i] != 0:
                out = "%s%s%sX^%s" % (out, sign, abs(self[i]), i)
        return out

    def gradient(self): return Polynomial([self[i] * i for i in range(1, len(self))])


def entering(n):
    vector = [float(input(" The term independent of x is: "))]
    [vector.append(float(input(" The coefficient of x to the power of " + str(i) + " is: "))) for i in range(1, n + 1)]
    return Polynomial(vector)
