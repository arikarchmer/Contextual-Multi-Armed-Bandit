import numpy as np
import matplotlib.pyplot as plt
from MAB.MAB import MAB
from Arm.Arm import Arm
from Thompson.ThompsonSampler import ThompsonSampler as ts

if __name__ =="__main__":

    a1 = Arm(0.5, 0)
    a2 = Arm(0.505, 1)
    a3 = Arm(0.503, 2)
    a4 = Arm(0.499, 3)
    a5 = Arm(.497, 4)

    optimal = 0.505

    arms = [a1, a2, a3, a4, a5]
    n_arms = len(arms)
    mab = MAB([1.0/n_arms for a in arms], [[0, 0] for a in arms])

    E = []
    res = []
    means = []
    choices = []
    p = {0: 0.5, 1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}
    sampler = ts(0)

    for itr in range(1000):
        nE = len(E)
        E_prime = []
        chosen = sampler.sample(E, E_prime, nE, p, n_arms, arms)

        reward = arms[chosen].select()
        E.append([chosen, reward])
        res.append(reward)
        means.append(float(sum(res))/len(res))
        choices.append([sum(l) for l in mab.observations])
        mab.recalibrate(reward, arms, arms[chosen])
    
    print mab.distribution
    print mab.observations

    print 
    plt.plot([[optimal,m] for m in means])
    plt.show()
    plt.plot(choices)
    plt.show()
            
