
import numpy.random as r

class BernoulliArm():

    def __init__(self, p, index):
        self.p = p
        self.index = index

    def select(self):
        if r.random() < self.p:
            return 1
        else:
            return 0
