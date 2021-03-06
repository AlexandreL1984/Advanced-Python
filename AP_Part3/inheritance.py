from AP_Part3.class_example import NumGen

class Stats(NumGen):
    def __init__(self, n):
        super().__init__(n)
        self.p = 2

    def mean(self, option='default'):
        if option == 'odd':
            self.nums = list(self.odd())
        elif option == 'even':
            self.nums = list(self.even())
        elif option == 'power':
            self.nums = list(self.power(self.p))

        return sum(self.nums) / len(self.nums)

stats = Stats(100)

stats.mean()

stats.mean(option='odd')

stats.mean(option='even')

stats.p = 4

stats.p

stats.mean(option='power')
