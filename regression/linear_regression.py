from random import uniform as a


class LR:
    def __init__(self, Xs, ys):
        self.coeff, self.Xs, self.ys, self.n, self.const = [a(0, 100) for _ in range(len(Xs[1]))], Xs, ys, len(Xs), 10

    def f(self, X): return self.const + sum(self[i] * X[i] for i in range(len(X)))

    def __dc(self, n):
        result = 2 * sum((self.f(self.Xs[i]) - self.ys[i]) * self.Xs[i][n]for i in range(self.n))/self.n
        return result

    def __dn(self):
        result = 2 * sum(self.f(self.Xs[i]) - self.ys[i] for i in range(self.n)) / self.n
        return result

    def regression(self):
        while sum([self.__dc(i) for i in range(len(self))]) > 0.01*len(self) or self.__dn() > 0.01:
            self.const += self.__dn() * -0.01
            self.coeff = [self.coeff[i]-self.__dc(i) * 0.01 for i in range(len(self))]
        return self.coeff, self.const

    def __getitem__(self, i): return self.coeff[i]

    def __setitem__(self, i, x): self.coeff[i] = x

    def __len__(self): return len(self.coeff)
