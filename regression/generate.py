import random as r


class DateGenerator:
    def __init__(self, theta):
        self.theta = theta

    def linear_generate(self, frequency=100, f='data.txt', fc=2):
        with open(f, 'w+') as file:
            for i in range(frequency):
                x = r.uniform(0, 10)
                y = r.gauss(self[0]+self[1]*x, fc)
                file.write("%s,%s\n" % (x, y))

    def __getitem__(self, i): return self.theta[i]
