import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor

class Model():

    def create_model(self, states, actions, rewards):
        #print 'states: ' + str(states)
        #print 'actions: ' + str(actions)
        #print 'rewards: ' + str(rewards)
 #       regr = linear_model.LinearRegression()
        regr = DecisionTreeRegressor(max_depth=5)

        states_chosen = [] 
        for a in range(len(actions)):
            action = actions[a]
            states_chosen.append([states[a][action]])

        states_chosen_arr = np.asarray(states_chosen, dtype=np.int32)
        sc_shape = states_chosen_arr.shape

        states_chosen_arr = np.asarray(states_chosen, dtype=np.float32)

        regr.fit(states_chosen, [[r] for r in rewards])
        return regr


    def predict(self, model, states, f):
        state = [[f(s)] for s in states]
        print state
        predictions = [model.predict(state)]
        print predictions
        predictions = [[p, predictions[0][p]] for p in range(len(predictions[0]))]
        d = {}
        for p in predictions:
            d[p[0]] = p[1]
        print 'MODEL: ' + str(d)
        return d
