import random as r


class LR:
    def __init__(self, x, y):
        self.m, self.c, self.x, self.y, self.n = r.uniform(1, 100), r.uniform(1, 100), x, y, len(x)

    def __dm(self): return 2 * sum((self.c + self.m * self.x[i] - self.y[i]) * self.x[i]for i in range(self.n)) / self.n

    def __dc(self): return 2 * sum(self.c + self.m * self.x[i] - self.y[i] for i in range(self.n)) / self.n

    def regression(self):
        while self.__dm() > 0.000001 or self.__dc() > 0.000001:
            self.c += self.__dc() * -0.0001
            self.m += self.__dm() * -0.0001
        return [self.c, self.m]
