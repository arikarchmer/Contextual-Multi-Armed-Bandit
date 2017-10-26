import numpy as np

class ThompsonSampler():

    def sample(self, E, E_prime, nE, n_arms, arms):

        predictions = {}
        print '\n|N| = ' + str(nE)
        if nE > 0:
            d = {}
            for i in range(nE):
                E_prime.append(E[np.random.randint(nE)])

            actions = []
            rewards = []
            states = []
            for item in E_prime:
                #print item
                actions.append(item[0])
                rewards.append(item[1])
                states.append(item[2])

            return [states, rewards, actions]
        
