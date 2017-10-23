import numpy as np
import matplotlib.pyplot as plt
from MAB.MAB import MAB
from Arm.Arm import Arm

if __name__ =="__main__":

    a1 = Arm(0.3, 0)
    a2 = Arm(0.87, 1)
    a3 = Arm(0.26, 2)
    a4 = Arm(0.65, 3)
    a5 = Arm(.65, 4)

    arms = [a1, a2, a3, a4, a5]
    n_arms = len(arms)
    mab = MAB([1.0/n_arms for a in arms], [[0, 0] for a in arms])

    res = []
    means = []
    for itr in range(2500):
        chosen = mab.choose_arm(arms)
        reward = chosen.select()
        res.append(reward)
        means.append(float(sum(res))/len(res))
        mab.recalibrate(reward, arms, chosen)
    
    print mab.distribution
    print mab.observations

    plt.plot(means)
    plt.show()
            
