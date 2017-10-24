
import numpy.random as r

class NormalArm():

    def __init__(self, mu, sigma, index):
        self.mu = mu
        self.sigma = sigma
        self.index = index

    def select(self):
        return r.normal(self.mu, self.sigma)
