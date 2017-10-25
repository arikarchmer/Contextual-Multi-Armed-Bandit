import numpy as np

class ThompsonSampler():

    def __init__(self, n):
        self.n = n

    def sample(self, E, E_prime, nE, p, n_arms, arms):

        print '|N| = ' + str(nE)
        if nE > 0:
            d = {}
            for i in range(nE):
                E_prime.append(E[np.random.randint(nE)])
            
            for item in E_prime:
                if item[0] not in d:
                    d[item[0]] = [item[1]]
                else:
                    d[item[0]].append(item[1])
            for k, v in d.iteritems():
                p[k] = float(sum(v))/len(v)

            print sorted(p.iteritems(), key=lambda (k,v): (v,k))
            chosen = sorted(p.iteritems(), key=lambda (k,v): (v,k))[len(p) - 1][0]

        else:
            chosen = arms[np.random.randint(n_arms)].index

        return [chosen, p]
