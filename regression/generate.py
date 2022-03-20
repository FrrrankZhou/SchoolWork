import random as r


class DateGenerator:
    def __init__(self, theta, const=0):
        self.theta, self.noise = theta, const

    def linear_generate(self, frequency=100, f='data.txt', fc=2):
        with open(f, 'w+') as file:
            for i in range(frequency):
                X = [r.uniform(0, 10)for _ in range(len(self))]
                y = r.gauss(self.noise+sum(self[i]*X[i]for i in range(len(self))), fc)
                file.write("%s,%s\n" % (" ".join([str(x) for x in X]), y))

    def __getitem__(self, i): return self.theta[i]

    def __len__(self): return len(self.theta)
