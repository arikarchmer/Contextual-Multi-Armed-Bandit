import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Arm.Bernoulli import BernoulliArm as Bernoulli
from Arm.Normal import NormalArm as Normal
from Thompson.ThompsonSampler import ThompsonSampler as ts
from Model.Model import Model

def createArms():

    a1 = Normal(np.random.randint(-3,4), np.random.randint(1,2), 0)
    a2 = Normal(np.random.randint(-3,4), np.random.randint(1,2), 1)
    a3 = Normal(np.random.randint(-3,4), np.random.randint(1,2), 2)
    a4 = Normal(np.random.randint(-3,4), np.random.randint(1,2), 3)
    a5 = Normal(np.random.randint(-3,4), np.random.randint(1,2), 4)

    return [a1, a2, a3, a4, a5]

if __name__ =="__main__":

    f = lambda x: x**3 + 2

    model = Model()

    E = []
    res = []
    means = []
    mus = []
    avg_mus = []
    mus_chosen = []
    avg_mus_chosen = []
    totals = []
    choices = []
    sampler = ts()
    
    for itr in range(1000):
        arms = createArms()
        n_arms = len(arms)
        
        nE = len(E)
        E_prime = []
        
        #sample from experience set E and choose best arm from estimated probabilities
        if nE > 0:
            sample = sampler.sample(E, E_prime, nE, n_arms, arms)
            states = sample[0]
            rewards = sample[1]
            actions = sample[2]

            curr_model = model.create_model([[f(s) for s in state] for state in states], actions, rewards)
            predictions = model.predict(curr_model, states, f)

            predictions_list = sorted(predictions.iteritems(), key=lambda (k,v): (v,k))
            #print predictions
            chosen = predictions_list[len(predictions_list) - 1][0]
            print 'CHOSEN: ' + str((chosen, predictions[chosen]))
        else:
            chosen = np.random.randint(0,5)
        
        reward = arms[chosen].select()
        print 'REWARD WAS: ' + str(reward)
        E.append([chosen, reward, [a.mu for a in arms]])
        res.append(reward)
        mus_chosen.append(arms[chosen].mu)
        avg_mus_chosen.append(float(sum(mus_chosen))/len(mus_chosen))
        totals.append(sum(res))
        means.append(float(sum(res))/len(res))
        mus.append(sum([a.mu for a in arms])/len(arms))
        avg_mus.append(float(sum(mus))/len(mus))

    print
    print 'AVG MU: ' + str(avg_mus[-1])
    print 'AVG MU CHOSEN: ' + str(avg_mus_chosen[-1])
    print 'AVG REWARD: ' + str(means[-1])
    print 'TOTAL REWARD: ' + str(sum(res))

    # average reward over time
    plt.plot(means, label="mean reward")
    plt.plot(avg_mus_chosen, label="avg mu chosen")
    plt.plot(avg_mus, label="avg mu")
    plt.legend(bbox_to_anchor=(0.5, 1), loc=1)
    plt.show()
    # total reward over time
    plt.plot(totals)
    plt.show()
            
