#function computeCost
import numpy as np
#file: functions.py
def predict(X,Theta):
	return X @ Theta
def computeCost(X,y,Theta):
	predicted = predict(X,Theta)
    #function computeCost
    sqr_error = (predicted - y) ** 2
    #function computeCost
    sum_error = np.sum(sqr_error)
    #function computeCost
    m = np.size(y)
    J = (1/(2*m))*sum_error
    return J
