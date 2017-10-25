
import numpy as np

class MAB():

    def __init__(self, dist, obs):
        self.distribution = dist
        self.observations = obs

        
    def choose_arm(self, arms):
        self.distribution = [np.random.beta(self.observations[a.index][0] + 1, self.observations[a.index][1] + 1) for a in arms]       
        return arms[self.distribution.index(max(self.distribution))]


    def recalibrate(self, reward, arms, a):
        if reward:
            self.observations[a.index][0] += 1
        else:
            self.observations[a.index][1] += 1          
        
        self.distribution = [np.random.beta(self.observations[a.index][0] + 1, self.observations[a.index][1] + 1) for a in arms] 
        #print self.distribution
        print
    
