import numpy as np
import matplotlib.pyplot as plt
from MAB.MAB import MAB
from Arm.Bernoulli import BernoulliArm as Bernoulli
from Arm.Normal import NormalArm as Normal
from Thompson.ThompsonSampler import ThompsonSampler as ts

if __name__ =="__main__":

    a1 = Normal(-10, 1, 0)
    a2 = Normal(0.1, 5, 1)
    a3 = Normal(0, 5, 2)
    a4 = Normal(-10, 1, 3)
    a5 = Normal(-0.1, 5, 4)

    optimal = 0.43

    arms = [a1, a2, a3, a4, a5]
    n_arms = len(arms)
    mab = MAB([1.0/n_arms for a in arms], [[0, 0] for a in arms])

    E = []
    res = []
    means = []
    choices = []
    p = {0: 0.5, 1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}
    averages = []
    sampler = ts(0)

    for itr in range(1000):
        nE = len(E)
        E_prime = []
        
        #sample from experience set E and choose best arm from estimated probabilities
        x = sampler.sample(E, E_prime, nE, p, n_arms, arms)
        chosen = x[0]
        p = x[1]

        l = []
        for k, v in p.iteritems():
            l.append(v)
        averages.append(l)
        
        reward = arms[chosen].select()
        E.append([chosen, reward])
        res.append(reward)
        means.append(float(sum(res))/len(res))
        choices.append([sum(l) for l in mab.observations])
        mab.recalibrate(reward, arms, arms[chosen])
    
    print p
    print len(averages)
    print choices[-1]

    print
    # average overall reward vs time
    plt.plot([[optimal, m] for m in means])
    plt.show()
    # average reward from each arm vs time
    plt.plot(averages)
    plt.show()
    # total count of times pulled for each arm vs time
    plt.plot(choices)
    plt.show()
            
